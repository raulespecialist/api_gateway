from django.shortcuts import render
from .models import Email
from rest_framework.views import APIView
from .serializers import EmailSerializer, EmailListSerializer
import requests
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from connectors.user import UserConnector
from django.utils import timezone
import json
from django.forms.models import model_to_dict


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

class UserListView(APIView):
    serializer_class = EmailSerializer
    queryset = Email.objects.all()
    pagination_class = StandardResultsSetPagination
    
    def get_serializer_class(self):
        if self.action == 'list':
            return EmailListSerializer
        return EmailSerializer
    
    def post(self, request, *args, **kwargs):
        parametros = request.POST
        email='email=' + request._full_data['user_email']
        response = UserConnector(email).get_user_data()
        obgs = response[1]['results']
        if len(obgs) == 0:
            user_email = self.request.POST.get('user_email')
            email_stat = ''
            email_scor = 0
            email_valid = ''
            frau = ''
        else:
            obg = response[1]['results'][0]

            user_email = self.request.POST.get('user_email')
            email_stat = obg.get('email_status')
            email_scor = obg.get('email_score')
            email_valid = obg.get('valid_email')
            frau = obg.get('fraud')

        NewEmail = Email(
            user_email = user_email,
            user_phone_number = self.request.POST.get('user_phone_number'),
            user_device_id = request.META.get('HTTP_DEVICE', ''),
            lat = self.request.POST.get('lat'),
            lng = self.request.POST.get('lng'),
            user_address = self.request.POST.get('user_address'),
            creation_date = timezone.now(),
            email_status = email_stat,
            email_score = email_scor,
            valid_email = email_valid,
            fraud = frau
        )
        NewEmail.save()
        serializer = EmailSerializer(NewEmail)
        return Response(serializer.data)

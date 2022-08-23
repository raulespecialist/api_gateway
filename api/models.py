from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.

class Email(models.Model):
    user_email = models.CharField(primary_key=True, max_length=200)
    user_phone_number = models.IntegerField(blank=True, null=True)
    user_device_id = models.CharField(max_length=200)#request.META.get('HTTP_DEVICE', '')
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lng = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    user_address = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=None, blank=True, null=True)
    email_status = models.BooleanField(default=None, blank=True, null=True)
    email_score = models.IntegerField(blank=True, default=0)
    valid_email = models.BooleanField(default=None, blank=True, null=True)
    fraud = models.BooleanField(default=None, blank=True, null=True)
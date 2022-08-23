from django.contrib import admin
from django.urls import include, path
#from rest_framework import routers
from api import views

#router = routers.DefaultRouter()
#router.register(r'user', views.EmailViewSet, 'users')

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/', include(router.urls)),
    path(
        "users/",
        views.UserListView.as_view(),
        name="user-list",
        )
]
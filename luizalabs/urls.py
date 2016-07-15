from django.conf.urls import url, include
from django.contrib import admin
from django.shortcuts import redirect
from rest_framework import routers
from employee import views


urlpatterns = [
    url(r'^$', lambda _: redirect('admin:index')),
    url(r'^admin/', admin.site.urls),
    url(r'^employee/', include('employee.urls')),
]
#Change the Site header
admin.site.site_header = 'Luizalabs Employee Manager'

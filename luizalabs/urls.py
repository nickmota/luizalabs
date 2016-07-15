from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from employee import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employee/', include('employee.urls')),
]

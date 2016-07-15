# coding: utf-8
from __future__ import unicode_literals
from django.conf.urls import url
from employee.views import EmployeeList


urlpatterns = [
    url(r'^$', EmployeeList.as_view(), name='employee'),
]

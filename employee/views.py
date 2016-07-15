# coding: utf-8
from __future__ import unicode_literals
from rest_framework import generics
from employee.models import Employee
from employee.serializers import EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):

    queryset = Employee.objects.all().order_by('name')
    serializer_class = EmployeeSerializer

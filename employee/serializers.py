# coding: utf-8
from __future__ import unicode_literals
from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')

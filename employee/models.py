#coding: utf-8
from __future__ import unicode_literals
from django.db import models


class Employee(models.Model):

    name = models.CharField('Name',max_length=50)
    email = models.EmailField('E-mail',max_length=200)
    department = models.CharField('Department',max_length=100)

    def __str__(self):
        return self.name

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Mentor(models.Model):
    user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    area = models.CharField(max_length=250)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    #user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    dob = models.DateField()
    standard = models.IntegerField()
    grade = models.IntegerField()
    area = models.CharField(max_length=250)
    mentor_assigned = models.ForeignKey(Mentor, default=None, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.OneToOneField(User, default=0, on_delete=models.CASCADE)
    #name = models.CharField(max_length=250)
    age = models.IntegerField()
    area = models.CharField(max_length=250)
    #qualifications = models.ForeignKey(Qualifications,default=0)
    # time_free


class Event (models.Model):
    name = models.CharField(max_length=250) #name of the event
    date = models.IntegerField()

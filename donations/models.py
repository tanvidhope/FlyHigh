from django.db import models

# Create your models here.

class donor(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    money_donated = models.IntegerField()
    donation_date = models.DateField() #automated

class donations(models.Model):
    name = models.CharField(max_length=250) # name of the thing to donateb to
    monthly_goal = models.DecimalField(decimal_places=2,max_digits=2)
    amt_raised = models.DecimalField(decimal_places=2,max_digits=2)
    goal_acheived = models.DecimalField(decimal_places=2,max_digits=2)





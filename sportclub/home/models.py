from typing import Match
from django.db import models
# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.CharField(max_length=50,primary_key=True)
    subject=models.CharField(max_length=500)
    class Meta:
        db_table="contact"

class Register(models.Model):
    tname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    pnumber=models.CharField(max_length=50)
    tmember=models.CharField(max_length=50)
    sports=models.CharField(max_length=50)
    agroup=models.CharField(max_length=50)
    team=models.CharField(max_length=50)
    Match=models.CharField(max_length=50)
    class Meta:
        db_table="register"
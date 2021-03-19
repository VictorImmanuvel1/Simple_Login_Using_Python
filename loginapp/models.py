from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    psd = models.CharField(max_length=30)

class Admin(models.Model):
    uname = models.CharField(max_length=30)
    psd = models.CharField(max_length=30)
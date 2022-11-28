from statistics import mode
from django.db import models
from django.conf import settings
#from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

class Movie (models.Model):
    title = models.CharField(max_length = 50)
    imgurl = models.CharField(max_length = 50)
    imgurl2 = models.CharField(max_length = 50 , null = True)
    description = models.TextField()
    genre = models.CharField(max_length = 50)
    numofmin = models.IntegerField()
    numofseats = models.IntegerField()
     
    def __str__(self):
        return self.title

class Viewer (models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    movie  = models.CharField(max_length = 255)
    numofseats = models.IntegerField()
    phonenumber = models.CharField(max_length = 12)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

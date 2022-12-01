from statistics import mode
from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.

class Movie (models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 50)
    imgurl = models.CharField(max_length = 250)
    imgurl2 = models.CharField(max_length = 250 , null = True)
    description = models.TextField()
    genre = models.CharField(max_length = 50)
    numofmin = models.IntegerField()
    numofseats = models.IntegerField()
    year = models.CharField(max_length = 4)
    director = models.CharField(max_length = 255)
     
    def __str__(self):
        return self.title

class Viewer (models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    movie_id = models.CharField(max_length = 1000)
    movie  = models.CharField(max_length = 255)
    numofseats = models.IntegerField()
    phonenumber = models.CharField(max_length = 11)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname}'

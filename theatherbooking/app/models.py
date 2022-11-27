from statistics import mode
from django.db import models
from django.conf import settings
#from phonenumber_field.modelfields import PhoneNumberField
from django.db import models

# Create your models here.

class Movie (models.Model):
    title = models.CharField(max_length = 50)
    imgurl = models.CharField(max_length = 50)
    description = models.CharField(max_length = 250)
    genre = models.CharField(max_length = 50)
    starttime = models.DateTimeField()    
    
    def __str__(self):
        return self.title
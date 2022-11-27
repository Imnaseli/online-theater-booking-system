from django.shortcuts import render
#from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate , login , logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.

def home(request):
    movie  = Movie.objects.all() 
    context = {'movies' : movie , 'count' : movie} 
    return render (request , "home.html" , context ) 
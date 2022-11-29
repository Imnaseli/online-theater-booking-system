from multiprocessing import context
from pydoc import describe
from django.shortcuts import render
from .forms import *
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

@login_required(login_url = 'signin')
def signout (request):
    logout(request)
    return redirect('home')

def signin(request):
    form = SigninForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('home')
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request , username=username , password=password)
        if user != None:
            login(request,user)
            return redirect('home')
        else:
            request.session['invalid_user'] = 1
    context = {'form':form}
    return render(request , 'signin.html', context)

def signup (request):
    form = SignupForm(request.POST or None)
    if request.user.is_authenticated:
        return redirect('home')
    if form.is_valid():
        username = form.cleaned_data.get('username')
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        
        if password == password2:
            User = get_user_model()
            try:
                user = User.objects.create_user(username ,  email , password )
                user.first_name = first_name
                user.last_name = last_name
                user.save()
            except Exception as e:
                user = None
        
            if user != None:
                login(request , user)
                return redirect ('home')
            else:
                request.session['register_error'] = 1
    context = {'form':form}
    return render(request , 'signup.html', context)

def moviepage(request , movie_id):
    movie = Movie.objects.get(id = movie_id)
    movieid = Movie.objects.get(id=movie_id).id
    seats = 0
    data = Viewer.objects.all()
    for x in data:
        seats += x.numofseats 
    remainingseats = movie.numofseats - seats 

    context = {'movie':movie ,  'seats':remainingseats }
    return render(request , 'moviepage.html' , context) 

@login_required(login_url = 'signin')              
def addmovie(request):
    form = AddMovie()
    if request.method == 'POST':
        form = AddMovie(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            movie = Movie(
                title = cd['title'],
                imgurl = cd['imgurl'],
                imgurl2 = cd['imgurl2'],
                year = cd['year'],
                director = cd['director'],
                description = cd['description'],
                genre = cd['genre'],
                numofmin = cd['numofmin'],
                numofseats = cd['numofseats'],
                )
            movie.save()
            return redirect ('home')
        else:
            return redirect ('home')
    context = {'form':form}
    return render (request , 'addmovie.html' , context)


def bookmovie(request , movie_id):
    movie = Movie.objects.get(id = movie_id)
    movieid = Movie.objects.get(id=movie_id).id
    form = BookmovieForm()
    if request.method == 'POST':
        form = BookmovieForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            viewer = Viewer(
                firstname = cd['firstname'],
                lastname = cd['lastname'],
                phonenumber = cd['phonenumber'],
                numofseats = cd['numofseats'],
                movie = movie.title,
                movie_id = movieid
                )
            viewer.save()
            return redirect('home')
        else:
            return redirect('home')
    
    context = {'form':form ,}
    return render (request , 'bookmovie.html' , context)
            
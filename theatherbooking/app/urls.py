from . import views
from django.urls import include, path

urlpatterns = [
    path('' , views.home , name = 'home'),
    
    
    
    path('signup' , views.signup , name='signup'),
    path('signin' , views.signin , name='signin'),
    path('signout' , views.signout , name='signout'),

    path('moviepage/<int:movie_id>' , views.moviepage , name='moviepage'),
    path('addmovie' , views.addmovie , name='addmovie'),
    path('bookmovie/<int:movie_id>' , views.bookmovie , name='bookmovie'),

    path('deletemovie<int:movie_id>', views.deletemovie, name='deletemovie'),
]
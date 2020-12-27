from django.shortcuts import render
from django.http import HttpResponse
from .models import posts


# Create your views here.

 
def home(request) : #creating the home route for 
    context ={
        'article' : posts.objects.all()
    }
    return render(request, 'Blog/home.html' ,context) 

def about(request) :
    return render(request, 'Blog/about.html' ,{'title' : 'About'}) #directly passing dict for context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_about_me(request):
    return("Hello, About Me!")
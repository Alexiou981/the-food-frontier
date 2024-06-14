from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = 'recipes/recipes.html'
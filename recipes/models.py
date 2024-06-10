from django.db import models
from django.contrib.auth.models import User
from blog.models import POST_STATUS, APPROVAL_STATUS

# Create your models here.

CUISINE = (
    (0, "International"), 
    (1, "Mediterranean"), 
    (2, "Asian"), 
    (3, "Middle-Eastern"),
    (4, "European"),
    (5, "African"),
    (6, "American"),
    (7, "Latin-American"),
    (8, "Carribean"))

class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    ingredients = models.TextField()
    instructions = models.TextField()
    cuisine = models.IntegerField(choices=CUISINE, default=0)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    approval_status = models.IntegerField(choices=APPROVAL_STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)


class RecipeComment(models.Model):
    post = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commentor")
    body = models.TextField()
    approval_status = models.IntegerField(choices=APPROVAL_STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    

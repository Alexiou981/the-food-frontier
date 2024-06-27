from . import views
from django.urls import path

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.recipes_detail, name='recipes_detail'),
    path('recipe-form', views.users_recipe, name='recipe_form')
]
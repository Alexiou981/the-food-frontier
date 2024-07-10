from . import views
from django.urls import path
from .views import MyRecipesList

urlpatterns = [
    path('', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.recipes_detail, name='recipes_detail'),
    path('recipe-form', views.users_recipe, name='recipe_form'),
    path('edit_recipe/<slug:slug>/', views.recipe_edit, name='recipe_edit'),
    path('delete_recipe/<slug:slug>/', views.recipe_delete, name='delete_recipe'),
    path('my_recipes', MyRecipesList.as_view(), name='my_recipes'),
]
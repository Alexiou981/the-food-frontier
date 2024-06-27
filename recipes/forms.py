from .models import UsersRecipe
from django import forms


class RecipeForm(forms.ModelForm):
    class Meta:
        model = UsersRecipe
        fields = ('title', 'author', 'cuisine', 'ingredients', 'instructions')
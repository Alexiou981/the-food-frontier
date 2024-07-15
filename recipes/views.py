from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views import generic
from django.db.models import Q
from .models import Recipe
from .forms import RecipeForm, strip_html_tags

# Create your views here.
class RecipeList(LoginRequiredMixin, generic.ListView):
    template_name = 'recipes/recipes.html'
    paginate_by = 6
    """ 
    This fucntion was created with the help of
    Complex lookups with Q object from the 
    Django documentation website here:
    https://docs.djangoproject.com/en/5.0/topics/db/queries/#complex-lookups-with-q-objects

    It ensures that pending recipes only appear to
    the author of them, and the rest of the users
    don't get to see the new recipe until it's 
    approved by the admin.
    """
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Recipe.objects.filter(Q(approval_status=1) | Q(author=user))
        else:
            return Recipe.objects.filter(approval_status=1)


class MyRecipesList(LoginRequiredMixin, generic.ListView):
    template_name = 'recipes/my_recipes.html'
    paginate_by = 6

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


@login_required
def CuisineView(request, cuisine):
    """
    This function was created with the help of Codemy.com
    in this tutorial: https://www.youtube.com/watch?v=PTsljbR-Cmo&t=197s
    """
    CUISINE_CHOICES = {
        'mediterranean': 0,
        'asian': 1,
        'middle-eastern': 2,
        'european': 3,
        'african': 4,
        'american': 5,
        'latin-american': 6,
        'caribbean': 7,
        'desserts': 8
    }

    cuisine_int = CUISINE_CHOICES.get(cuisine.lower())
    
    cuisine_recipes = Recipe.objects.filter(cuisine=cuisine_int)
    return render(request, 'recipes/filtered_cuisines.html', {"cuisine": cuisine, 'cuisine_recipes': cuisine_recipes})
    

@login_required
def recipes_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "recipes/recipes_detail.html",
        {"recipe": recipe},
    )


@login_required
def users_recipe(request):

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe_form.save()
            messages.add_message(request, messages.SUCCESS,
            "Recipe submitted and is awaiting for approval")
    recipe_form = RecipeForm()

    return render(
        request,
        "recipes/recipe_form.html",
        {
            "recipe_form": recipe_form
        }
    )


@login_required
def recipe_edit(request, slug):
    """
    View to edit recipes
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST, instance=recipe)
        if recipe_form.is_valid() and recipe.author == request.user:
            updated_recipe = recipe_form.save(commit=False)
            updated_recipe.approval_status = False
            updated_recipe.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe updated and awaiting approval')
            return redirect('recipes')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating recipe!')
    else:
        recipe_form = RecipeForm(instance=recipe)

    return render(request, 'recipes/recipe_form.html', {'recipe_form': recipe_form})


@login_required
def recipe_delete(request, slug):
    """
    View to delete recipes
    """
    recipe_to_delete = Recipe.objects.get(slug=slug)

    if recipe_to_delete.author == request.user:
        recipe_to_delete.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe deleted successfully!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own recipes.')
    
    return HttpResponseRedirect(reverse('recipes'))
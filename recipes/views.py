from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    template_name = 'recipes/recipes.html'
    paginate_by = 6


def recipes_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Recipe.objects.filter(approval_status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "recipes/recipes_detail.html",
        {"recipe": recipe},
    )


def users_recipe(request):

    if request.method == "POST":
        recipe_form = RecipeForm(data=request.POST)
        if recipe_form.is_valid():
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
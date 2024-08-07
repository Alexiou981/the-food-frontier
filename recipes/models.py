from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from blog.models import POST_STATUS, APPROVAL_STATUS

# Create your models here.

CUISINE = (
    (0, "Mediterranean"),
    (1, "Asian"),
    (2, "Middle-Eastern"),
    (3, "European"),
    (4, "African"),
    (5, "American"),
    (6, "Latin-American"),
    (7, "Caribbean"),
    (8, "Desserts"))


class Recipe(models.Model):
    """
    Recipe model for existing recipes and for any new recipes
    submitted by the recipe form.
    Stores entries related to :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    excerpt = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="recipes", blank=True, null=True)
    ingredients = models.TextField()
    instructions = models.TextField()
    cuisine = models.IntegerField(choices=CUISINE, default=0)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    approval_status = models.IntegerField(choices=APPROVAL_STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.title}'
        return f'{self.cuisine}'

    def save(self, *args, **kwargs):
        """
        This function automatically uses the title to turn it into a slug.
        Function provided by Giancarlo Ventura here:
        https://stackoverflow.com/questions/70601191/how-to-auto-populate-slug-field-in-django-forms
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

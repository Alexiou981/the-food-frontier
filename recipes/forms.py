from django import forms
from .models import Recipe
from bs4 import BeautifulSoup



def strip_html_tags(text):
    """
    This function was created using following the 
    beautifulsoup documentation which is found here:
    https://www.crummy.com/software/BeautifulSoup/bs4/doc/

    Utility function that ensures that any html tags get removed 
    and only the text appears on the field when user edits an existing 
    recipe.
    """
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()


class RecipeForm(forms.ModelForm):
    class Meta:
        """
        SummernoteWidget was imported and used for the recipe form
        submission and editing. Information about usage and 
        implementation was found here:
        https://github.com/summernote/django-summernote
        """
        model = Recipe
        fields = ['title', 'excerpt', 'ingredients', 'instructions', 'cuisine']
        widgets = {
            'excerpt': forms.Textarea(attrs={'rows': 4}),
            'ingredients': forms.Textarea(attrs={'rows': 6}),
            'instructions': forms.Textarea(attrs={'rows': 6}),
        }


def __init__(self, *args, **kwargs):
    """ 
    Function takes initial value of fields
    and strips any html tags found it it only 
    to display text to user who wants to edit recipe.
    """
    super(RecipeForm, self).__init__(*args, **kwargs)
    if self.instance:
        self.fields['excerpt'].initial = strip_html_tags(self.instance.excerpt)
        self.fields['ingredients'].initial = strip_html_tags(self.instance.ingredients)
        self.fields['instructions'].initial = strip_html_tags(self.instance.instructions)

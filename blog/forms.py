from .models import PostComment
from django import forms


class PostCommentForm(forms.ModelForm):
    """
    Taken from the Codestar project by Code Institute
    """
    class Meta:
        model = PostComment
        fields = ('body',)

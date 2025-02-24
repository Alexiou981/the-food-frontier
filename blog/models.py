from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

POST_STATUS = ((0, "Draft"), (1, "Published"))
APPROVAL_STATUS = ((0, "Not-Approved"), (1, "Approved"))


# Create your models here.
class Post(models.Model):
    """
    Model taken from the Codestar project by Code Institute.
    Stores post entries which are related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="blog_posts")
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    approval_status = models.IntegerField(choices=APPROVAL_STATUS, default=0)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"

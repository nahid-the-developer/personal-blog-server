from django.db import models

from authentication.models import Account


# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='blogs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    keyword = models.TextField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='blog_posts')

    def __str__(self):
        return self.title

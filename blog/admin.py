from django.contrib import admin
from django.forms import ModelForm
from tinymce.widgets import TinyMCE

from blog.models import BlogPost


# Register your models here.

class BlogForm(ModelForm):
    class Meta:
        model = BlogPost
        exclude = ['author']
        widgets = {'description': TinyMCE(attrs={'cols': 80, 'rows': 30})}


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'created_at', 'updated_at')
    form = BlogForm


admin.site.register(BlogPost, BlogAdmin)

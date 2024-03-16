from django_filters import rest_framework as filters

from blog.models import BlogPost


class BlogPostFilter(filters.FilterSet):
    title = filters.CharFilter(field_name='title', lookup_expr='icontains')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains')
    keyword = filters.CharFilter(field_name='keyword', lookup_expr='icontains')

    class Meta:
        model = BlogPost
        fields = ['title', 'description', 'keyword']

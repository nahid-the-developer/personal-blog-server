from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from authentication.viewset import AuthenticationViewSet
from blog.viewset import BlogPostViewSet

router = routers.DefaultRouter()
router.register(r'auth', AuthenticationViewSet, basename='authentication')
router.register(r'blogs', BlogPostViewSet, basename='blogs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

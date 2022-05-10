from django.contrib import admin
from django.urls import path
import techBlogPosts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',techBlogPosts.views.index,name='index')
]

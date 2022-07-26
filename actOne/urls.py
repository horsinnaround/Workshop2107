"""actOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from django.urls import url
from blog import views as blog_views
urlpatterns = [
    path('post/', blog_views.post),
    path('post/about/', blog_views.about),
    path('about/', blog_views.about), 
    re_path(r'^about/(.*)$', blog_views.about),
    path('admin/', admin.site.urls),
    re_path(r'^post/(.*)$', blog_views.post),
    path('', blog_views.index),
    # path('admin/', admin.site.urls),
]
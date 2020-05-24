"""django_prj07 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from blog.auth import views as auth_views
from blog.views import list_my_posts
from blog import urls as blog_urls

urlpatterns = [
    path('', list_my_posts, name="home" ),
    path('login/', auth_views.user_login, name="login"),
    path('logout/', auth_views.user_logout, name="logout"),
    path('register/', auth_views.user_register, name="register"),
    path('admin/', admin.site.urls),
    path('blog/', include(blog_urls)),
    # path('blog/', include(blog_urls, namespace="blog")),
]

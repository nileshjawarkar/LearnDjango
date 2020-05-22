from django.urls import path
from .views import home, user_login

app_name = "blog"

urlpatterns = [
    path('home/', home, name="home"),
]

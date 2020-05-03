from rest_framework import routers
from .views import BookViewset
from django.urls import path, include

routs = routers.DefaultRouter()
routs.register( "books", BookViewset )

urlpatterns = [
    path('', include(routs.urls)),
]

from django.urls import path
from app01 import views as app01_views

app_name = 'app01'

urlpatterns = [
    path('', app01_views.index, name="index" ),
    path('blds/', app01_views.list_blds, name="blds" ),
    path('flats/', app01_views.list_flats, name="flats" ),
]

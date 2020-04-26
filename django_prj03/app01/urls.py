from django.urls import path
from app01 import views as app01_views

app_name = 'app01'

urlpatterns = [
    path('', app01_views.index, name="index" ),
    path('blds/', app01_views.blds, name="blds" ),
    path('flats/', app01_views.flats, name="flats" ),    
    path('addblds/', app01_views.add_blds, name="addblds" ),
    path('addflats/', app01_views.add_flats, name="addflats" ),
]

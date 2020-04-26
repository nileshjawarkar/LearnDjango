from django.shortcuts import render
from django.http import request

def index( request ) :
    return render( request, "index.html")

def list_blds( request ) :
    return render( request, "blds.html")

def list_flats( request ) :
    return render( request, "flats.html")


from django.shortcuts import render
from django.http import request
from django import forms
from app01.models import Building, Flat
from app01.forms import BuildingForm, FlatForm

def index( request ) :
    return render( request, "index.html")

def blds( request ) :
    all_blds = Building.objects.all()
    return render( request, "blds.html", {"blds" : all_blds })

def flats( request ) :
    all_flats = Flat.objects.all()
    return render( request, "flats.html", {"flats" : all_flats })

def add_blds( request ) :
    bld_form = None
    isPost = (request.method == "POST")
    add_successful = False
    if isPost :
        bld_form = BuildingForm( request.POST )
        if bld_form.is_valid() :
            bld_form.save()
            add_successful = True
        # else:
        #    raise forms.ValidationError("Please check your inputs")
    
    if not isPost or add_successful :
        bld_form = BuildingForm()
    return render( request, "addblds.html", {"form" : bld_form })

def add_flats( request ) :
    isPost = (request.method == "POST")
    add_successful = False    
    if isPost :
        flats_form = FlatForm( request.POST )
        if flats_form.is_valid() :
            flats_form.save()
            add_successful = True          
        # else:
        #    raise forms.ValidationError("Please check your inputs")
    
    if not isPost or add_successful :
        flats_form = FlatForm()    
    return render( request, "addflats.html", {"form" : flats_form })


from django.shortcuts import render
from django.http import request
from django import forms
from app01.forms import BuildingForm, FlatForm

def index( request ) :
    return render( request, "index.html")

def list_blds( request ) :
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
    return render( request, "blds.html", {"form" : bld_form })

def list_flats( request ) :
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
    return render( request, "flats.html", {"form" : flats_form })


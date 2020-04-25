from django.shortcuts import render
from django.http import request
from app01.forms import TestForm

def info( request ) :
    return render( request, "app01/info.html", {"info" : "Information successfuly validated"})

def form_test( request ) :

    test_form = TestForm()
    if request.method == "POST" :

        test_form = TestForm(  request.POST )
        if test_form.is_valid() :

            print("Form validation successful")
            print( "First name : ", test_form.cleaned_data["first_name"])
            print( "Last name : ", test_form.cleaned_data["last_name"])
            print( "Age : ", test_form.cleaned_data["age"])
            print( "Email : ", test_form.cleaned_data["email"])

            return info( request )
        else:
            print("Form validation failed")      
    
    return render( request, "app01/form_test.html", {"form" : test_form })


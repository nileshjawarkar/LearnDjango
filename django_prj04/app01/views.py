from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from app01.forms import UserForm, UserProfileForm

def index( request ) :
    return render( request, "app01/index.html")

def user_login( request ) :

    err_message = ""
    if request.method == "POST" :
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            return HttpResponseRedirect( reverse("index") )
        else :
           err_message = "Invalid credentials" 
    
    return render( request, "app01/login.html", { "err_message" : err_message })

def user_logout( request ) :
    logout( request )
    return HttpResponseRedirect( reverse("index") )


def register( request ) :
    registered = False

    if request.method == "POST" :
        user_form = UserForm( request.POST )
        user_profile_form = UserProfileForm( request.POST )

        if user_form.is_valid() and user_profile_form.is_valid() :

            user = user_form.save(commit=False)
            user.set_password( user.password )
            user.save()

            user_profile = user_profile_form.save(commit=False)
            user_profile.user = user

            if 'profile_pic' in request.FILES :
                user_profile.profile_pic = request.FILES['profile_pic']

            user_profile.save()
            registered = True
        
        else:
            print( user_form.errors, user_profile_form.errors )
    else:

        user_form = UserForm()
        user_profile_form = UserProfileForm()

    return render( request, "app01/register.html", { "registered" : registered , "user_form" : user_form, "user_profile_form" : user_profile_form })




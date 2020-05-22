from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

from .forms import UserAuthForm, UserRegistrationForm

def home( request ) :
    return render( request, "blog/home.html")

@login_required
def user_logout( request ) :
    logout(request)
    return HttpResponseRedirect("/")


def user_login( request ) :
    form = None
    if request.method == "POST" :
        form = UserAuthForm(request.POST)
        if form.is_valid() :
            login(request, form.user)
            return HttpResponseRedirect("/")
    else :
        form = UserAuthForm()
    return render(request, "blog/generic_form.html", {"form" : form, "form_title" : "User login", "form_submit_value" : "Login"} )

def user_register( request ) :
    if request.method == "POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            return HttpResponseRedirect("/")
    else :
        form = UserRegistrationForm()

    return render(request, "blog/generic_form.html", {"form" : form, "form_title" : "User registration", "form_submit_value" : "Register"} )
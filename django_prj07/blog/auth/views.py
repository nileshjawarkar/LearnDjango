from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from blog.auth.forms import UserAuthForm, UserRegistrationForm

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
    return render(request, "blog/user_form.html", {"form" : form, "form_title" : "Sign in", "form_submit_value" : "Login"} )

def user_register( request ) :
    if request.method == "POST" :
        form = UserRegistrationForm(request.POST)
        if form.is_valid() :
            user = form.save()
            return HttpResponseRedirect("/")
    else :
        form = UserRegistrationForm()

    return render(request, "blog/user_form.html", {"form" : form, "form_title" : "Sign up", "form_submit_value" : "Register"} )


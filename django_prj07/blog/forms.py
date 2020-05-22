from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from .models import Post, Comment

class UserAuthForm( forms.Form ) :
    user = None

    username = forms.CharField(label="User name", widget=forms.TextInput(attrs={"class" : "form-control"}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class" : "form-control"}))

    def clean( self ) :
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username is not None and password :
            self.user = authenticate(username=username, password=password)
            if self.user is None :
                raise forms.ValidationError("Invalid username or password")

class UserRegistrationForm( forms.ModelForm ) :
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class" : "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"class" : "form-control"}))
    class Meta() :
        model = User
        fields = ( "username", "first_name", "last_name" )
        widgets = {
            "username" : forms.TextInput(attrs={"class" : "form-control"}),
            "first_name" : forms.TextInput(attrs={"class" : "form-control"}),
            "last_name" : forms.TextInput(attrs={"class" : "form-control"}),
        }


    def clean_password2( self ) :
        pwd1 = self.cleaned_data.get("password")
        pwd2 = self.cleaned_data.get("password2")

        if pwd1 != pwd2 :
            raise forms.ValidationError("Both the password entered didnt match")
        return pwd2


    def save( self, commit=True ) :
        pwd = self.cleaned_data.get("password")
        user = super().save(commit=False)
        user.set_password( pwd )
        if commit :
            super().save()



class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("author", "title", "text")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", "text")
        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"})
        }

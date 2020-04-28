from django import forms
from app01.models import UserProfile
from django.contrib.auth.models import User

class UserForm( forms.ModelForm ) :
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta :
        model = User
        fields = ('username', 'email', 'password', )

class UserProfileForm( forms.ModelForm ) :
    profile_url = forms.URLField(label="Profile url", required=False)
    profile_pic = forms.ImageField(label="Profile picture", required=False)

    class Meta:
        model = UserProfile
        exclude = ("user",)



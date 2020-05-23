from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("title", "text")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"})
        }     

class PostFormReadonly(forms.ModelForm):

    class Meta():
        model = Post
        fields = ("title", "text")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "readonly" : True}),
            "text": forms.Textarea(attrs={"class": "form-control", "readonly" : True})
        }     


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ("author", "text")
        widgets = {
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"})
        }

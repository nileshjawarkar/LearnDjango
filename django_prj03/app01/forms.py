from django import forms
from app01.models import Building, Flat

class BuildingForm( forms.ModelForm ) :
    class Meta:
        model = Building
        fields = "__all__"

class FlatForm( forms.ModelForm ) :
    class Meta:
        model = Flat
        fields = "__all__"
from django import forms

class TestForm( forms.Form ) :
    first_name = forms.CharField( label="First name")
    last_name = forms.CharField( label="Last name")
    age = forms.IntegerField()
    email = forms.EmailField()
    reemail = forms.EmailField(label="Confirm your email")

    def clean( self ) :
        all_fileds = super().clean()
        if all_fileds["email"] != all_fileds["reemail"] :
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")

from django import forms
from .models import User

class RegistrationForm(forms.ModelForm):
    first_name       = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'First Name'})) 
    last_name        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'Last Name'}))
    username         = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'Name'}))
    email            = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'Email'}))
    phone_no         = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'Phone No'}))
    password         = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'Password'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','style':'border-color:lightblue;border-radius:16px','placeholder':'Confirm Password'}))
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','phone_no','password','checkbox']

    def clean(self):
        cleaned_data = super(RegistrationForm,self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password does not matched.'
            )
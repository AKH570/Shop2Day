from django import forms
from Orders.models import Order

class OrderForm(forms.ModelForm): # color pick from: https://htmlcolorcodes.com/color-names/
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px'}))
    phone_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px'}))
    country = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px'}))
    district = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'border-color:thistle;border-radius:10px'}))
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','phone_no','country','address','district']

        address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
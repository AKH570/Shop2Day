from django import forms
from Orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name','last_name','email','phone_no','country','address','district']

        address = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
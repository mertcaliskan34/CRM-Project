from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record, Order, Product

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'district', 'country']

class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model = Record
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'district', 'country']

class CreateOrderForm(forms.ModelForm):
    
    customer = forms.ModelChoiceField(queryset=Record.objects.all(), label="Select Customer")
    status = forms.ChoiceField(choices=Order.ORDER_STATUS_CHOICES, label="Order Status")
    
    class Meta:
        model = Order
        fields = ['order_number', 'customer', 'products', 'amount', 'status']
        
class UpdateOrderForm(forms.ModelForm):
    
    customer = forms.ModelChoiceField(queryset=Record.objects.all(), label="Select Customer")
    status = forms.ChoiceField(choices=Order.ORDER_STATUS_CHOICES, label="Order Status")
    
    class Meta:
        model = Order
        fields = ['order_number', 'customer', 'products', 'amount', 'status']
    
class CreateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        
class UpdateProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
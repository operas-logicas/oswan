from django import forms
from .models import Motorcycle

class AddMotorcycle(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = ['model', 'year', 'horsePower', 'transStyle', 'engineStyle', 'engineCapacity', 'price', 'productImage', 'description']
        widgets = {
            'model': forms.TextInput(attrs={'placeholder': 'Model'}),
            'year': forms.TextInput(attrs={'placeholder': 'Year'}),
            'horsePower': forms.TextInput(attrs={'placeholder': 'Horsepower'}),
            'transStyle': forms.TextInput(attrs={'placeholder': 'Trans Style'}),
            'engineStyle': forms.TextInput(attrs={'placeholder': 'Engine Style'}),
            'engineCapacity': forms.TextInput(attrs={'placeholder': 'Engine Capacity'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 5}),
            'price': forms.TextInput(attrs={'placeholder': 'Price'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

from django import forms
from .models import Farmer, Client, Produce

class ProduceForm(forms.ModelForm):
    class Meta:
        model = Produce
        fields = ['name', 'price']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = ['name', 'farm_name', 'location', 'contact', 'produce_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'farm_name': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'produce_type': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'contact', 'location', 'interested_produce']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'interested_produce': forms.TextInput(attrs={'class': 'form-control'}),
        }


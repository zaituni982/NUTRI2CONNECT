from django import forms
from .models import Farmer, Client

# Farmer Form
class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'  # include all fields

# Client Form
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'  # include all fields

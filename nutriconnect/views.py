from django.shortcuts import render, redirect, get_object_or_404
from .models import Farmer, Client
from .forms import FarmerForm, ClientForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Home view
def home(request):
    return render(request, 'nutriconnect/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    
    return render(request, 'nutriconnect/register.html', {'form': form})



# Farmer CRUD views
# List all farmers
def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'nutriconnect/farmer_list.html', {'farmers': farmers})

# Create a new farmer
def farmer_create(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('farmer_list')
    return render(request, 'nutriconnect/farmer_form.html', {'form': form})

# Update an existing farmer
def farmer_update(request, id):
    farmer = get_object_or_404(Farmer, id=id)
    form = FarmerForm(request.POST or None, instance=farmer)
    if form.is_valid():
        form.save()
        return redirect('farmer_list')
    return render(request, 'nutriconnect/farmer_form.html', {'form': form})

# Delete a farmer
def farmer_delete(request, id):
    farmer = get_object_or_404(Farmer, id=id)
    if request.method == "POST":
        farmer.delete()
        return redirect('farmer_list')
    return render(request, 'nutriconnect/farmer_confirm_delete.html', {'farmer': farmer})


# Client CRUD views
# List all clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'nutriconnect/client_list.html', {'clients': clients})

# Create a new client
def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'nutriconnect/client_form.html', {'form': form})

# Update an existing client
def client_update(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'nutriconnect/client_form.html', {'form': form})

# Delete a client
def client_delete(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'nutriconnect/client_confirm_delete.html', {'client': client})

# Create your views here.
# in nutriconnect/views.py

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django_daraja.mpesa.core import MpesaClient

def payment_stk_push(request):
    # This is the view that handles the payment request
    if request.method == 'POST':
        # 1. Get transaction details from the form
        phone_number = request.POST.get('phone') # Example: get phone from a form field
        amount = request.POST.get('amount')     # Example: get amount from a form field

        # Convert amount to an integer (M-Pesa API requires integers)
        amount = int(amount) 

        # 2. Initialize the Mpesa Client
        cl = MpesaClient()
        account_reference = 'NutriConnectPayment' 
        transaction_desc = 'Payment for Farmer Service'

        # This URL MUST be a public URL that M-Pesa can reach (use Ngrok for testing)
        # For now, use the host you set in settings.py + the library's built-in callback URL
        callback_url = f'{settings.MPESA_API_URL}/daraja/stk-push-callback/' 

        # 3. Initiate the STK Push
        response = cl.stk_push(
            phone_number=phone_number, 
            amount=amount, 
            account_reference=account_reference, 
            transaction_desc=transaction_desc, 
            callback_url=callback_url
        )
        
        # You will receive an immediate response (Success, Request accepted for processing)
        # The final transaction status comes via the callback_url later.
        return HttpResponse(response)
    
    # Render a simple form for testing the payment initiation
    return render(request, 'nutriconnect/payment_form.html')
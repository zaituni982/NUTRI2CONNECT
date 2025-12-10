from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Models & Forms
from .models import Farmer, Client, Produce, Offer, PurchaseOrder
from .forms import FarmerForm, ClientForm, ProduceForm

# Mpesa Client
from django_daraja.mpesa.core import MpesaClient


# --- CORE & AUTH VIEWS ---

def home(request):
    return render(request, 'nutriconnect/home.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('marketplace')
    else:
        form = UserCreationForm()
    return render(request, 'nutriconnect/register.html', {'form': form})


def marketplace(request):
    farmers = Farmer.objects.all()
    produce_list = Produce.objects.all()
    offers = Offer.objects.all()
    return render(request, "nutriconnect/marketplace.html", {
        "farmers": farmers,
        "produce_list": produce_list,
        "offers": offers,
    })


def farmer_produce(request, id):
    farmer = get_object_or_404(Farmer, id=id)
    produce_list = Produce.objects.filter(farmer=farmer)
    return render(request, 'nutriconnect/farmer_produce.html', {
        'farmer': farmer,
        'produce_list': produce_list
    })

@login_required
def add_produce(request, farmer_id):
    farmer = get_object_or_404(Farmer, id=farmer_id)
    form = ProduceForm(request.POST or None)
    
    if form.is_valid():
        produce = form.save(commit=False)
        produce.farmer = farmer
        produce.save()
        return redirect('farmer_produce', id=farmer.id)
    
    return render(request, 'nutriconnect/produce_form.html', {'form': form, 'farmer': farmer})


@login_required
def buy_produce(request, id):
    produce = get_object_or_404(Produce, id=id)
    farmer = produce.farmer
    return render(request, 'nutriconnect/buy_now.html', {
        'produce': produce,
        'farmer': farmer,
    })


# --- FARMER CRUD VIEWS ---

def farmer_list(request):
    farmers = Farmer.objects.all()
    return render(request, 'nutriconnect/farmer_list.html', {'farmers': farmers})


def farmer_create(request):
    form = FarmerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('farmer_list')
    return render(request, 'nutriconnect/farmer_form.html', {'form': form})


def farmer_update(request, id):
    farmer = get_object_or_404(Farmer, id=id)
    form = FarmerForm(request.POST or None, instance=farmer)
    if form.is_valid():
        form.save()
        return redirect('farmer_list')
    return render(request, 'nutriconnect/farmer_form.html', {'form': form})


def farmer_delete(request, id):
    farmer = get_object_or_404(Farmer, id=id)
    if request.method == "POST":
        farmer.delete()
        return redirect('farmer_list')
    return render(request, 'nutriconnect/farmer_confirm_delete.html', {'farmer': farmer})


# --- CLIENT CRUD VIEWS ---

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'nutriconnect/client_list.html', {'clients': clients})


def client_create(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'nutriconnect/client_form.html', {'form': form})


def client_update(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('client_list')
    return render(request, 'nutriconnect/client_form.html', {'form': form})


def client_delete(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'nutriconnect/client_confirm_delete.html', {'client': client})


# --- PRODUCE CRUD VIEWS (for Farmers) ---

@login_required
def produce_list(request):
    # For simplicity, show all produce for now
    produce_items = Produce.objects.all()
    return render(request, 'nutriconnect/produce_list.html', {'produce_items': produce_items})


@login_required
def produce_create(request):
    form = ProduceForm(request.POST or None)
    if form.is_valid():
        produce = form.save(commit=False)
        # Assign a farmer. Replace with your logic if Farmer is linked to User
        produce.farmer = Farmer.objects.first()  # For testing purposes
        produce.save()
        return redirect('produce_list')
    return render(request, 'nutriconnect/produce_form.html', {'form': form})


# --- PAYMENT VIEW (MPESA STK PUSH) ---

@login_required
def payment_stk_push(request):
    if request.method != 'POST':
        return HttpResponse("Invalid request.", status=405)

    produce_id = request.POST.get('produce_id')
    amount = request.POST.get('amount')
    phone = request.POST.get('phone')

    if not produce_id or not amount or not phone:
        return HttpResponse("Missing required fields.", status=400)

    produce = get_object_or_404(Produce, id=produce_id)
    farmer = produce.farmer

    try:
        amount = int(amount)
    except ValueError:
        return HttpResponse("Invalid amount.", status=400)

    order = PurchaseOrder.objects.create(
        client=request.user,
        produce=produce,
        farmer=farmer,
        amount=amount,
        phone_number=phone,
        status='PENDING'
    )

    cl = MpesaClient()
    callback_url = f"{settings.SITE_URL}/mpesa/callback/{order.id}/"

    cl.stk_push(
        phone_number=phone,
        amount=amount,
        account_reference=f"ORDER-{order.id}",
        transaction_desc="Produce Purchase Payment",
        callback_url=callback_url
    )

    return HttpResponse("STK Push Initiated. Check your phone.")


@csrf_exempt
def mpesa_callback(request, order_id):
    data = request.body.decode('utf-8')
    order = get_object_or_404(PurchaseOrder, id=order_id)

    try:
        import json
        mpesa_data = json.loads(data)
        receipt = mpesa_data["Body"]["stkCallback"]["CallbackMetadata"]["Item"][1]["Value"]
        order.mpesa_receipt = receipt
        order.status = "PAID"
    except Exception:
        order.status = "FAILED"

    order.save()
    return HttpResponse("Callback received successfully.")

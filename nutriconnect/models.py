from django.db import models
from django.contrib.auth.models import User


# Farmer Model
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    farm_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    produce_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.farm_name}"


# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    interested_produce = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.interested_produce}"


# Produce Model
class Produce(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='produces')

    def __str__(self):
        return self.name



class Offer(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer.farm_name} - {self.produce.name} ({self.quantity}) @ {self.price} KSH"



class PurchaseOrder(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('FAILED', 'Failed'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)

    amount = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    mpesa_receipt = models.CharField(max_length=50, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.client.username}"

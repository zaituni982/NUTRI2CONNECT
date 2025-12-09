from django.db import models

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

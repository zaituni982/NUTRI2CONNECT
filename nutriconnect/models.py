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


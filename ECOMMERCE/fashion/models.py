from django.db import models

class FashionItem(models.Model):
    name = models.CharField(max_length=100)  # Name of the fashion item
    brand = models.CharField(max_length=50)  # Brand name
    category = models.CharField(max_length=50)  # e.g., Shirt, Pants, Accessories
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price with two decimal precision
    stock_quantity = models.PositiveIntegerField()  # Quantity available in stock

    def __str__(self):
        return f"{self.name} - {self.category} ({self.brand})"

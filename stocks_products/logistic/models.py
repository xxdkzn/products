from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    warehouses = models.ManyToManyField(Warehouse, through='Stock')

    def __str__(self):
        return self.name


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    storage_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ('product', 'warehouse')

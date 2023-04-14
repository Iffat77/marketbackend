from django.db import models
from accounts.models import Profile
from products.models import Product

# Create your models here.
class Cart(models.Model):
    buyer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='InCart')
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.buyer.user.email}'s cart"



class InCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.buyer.user.email}'s cart"

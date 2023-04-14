from django.contrib import admin

# Register your models here.
from .models import Cart, InCart

admin.site.register(Cart)
admin.site.register(InCart)
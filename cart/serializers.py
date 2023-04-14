from rest_framework import serializers
from .models import Cart, InCart

class InCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = InCart
        fields = '__all__'
        
class CartSerializer(serializers.ModelSerializer):
    products = InCartSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
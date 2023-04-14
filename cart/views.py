from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Cart, InCart
from .serializers import CartSerializer, InCartSerializer

class CartView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return Cart.objects.get(buyer__user=user)
        #buyer__user=user means follow foreignkey from cart -> profile, then 1:1 from profile -> user

class InCartView(generics.ListCreateAPIView):
    serializer_class = InCartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        cart = Cart.objects.get(buyer__user=user)
        return InCart.objects.filter(cart=cart)
      
    def perform_create(self, serializer):
        user = self.request.user
        cart = Cart.objects.get(buyer__user=user)
        serializer.save(cart=cart)

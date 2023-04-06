from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from .models import Category, Product, Review

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
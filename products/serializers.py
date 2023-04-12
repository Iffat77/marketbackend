from rest_framework import serializers
from .models import Category, Product, Review
from accounts.serializers import ProfileSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    seller = ProfileSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = ProfileSerializer(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

from rest_framework import viewsets, permissions
from .models import Category, Product, Review
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework.response import Response

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        seller_id = request.query_params.get('seller_id')
        if seller_id is not None:
            queryset = Product.objects.filter(seller__id=seller_id)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return super().list(request)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticated]

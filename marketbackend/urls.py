from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from products.views import CategoryViewSet, ProductViewSet, ReviewViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include('accounts.urls')),
    path('market/', include(router.urls)),
    path('admin/', admin.site.urls),
     path('market/', include('cart.urls')),
]

# /market/products/?seller_id to products listed by a specific seller
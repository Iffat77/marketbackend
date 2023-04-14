from django.urls import path
from .views import CartView, InCartView

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/items/', InCartView.as_view(), name='cart-items'),
]

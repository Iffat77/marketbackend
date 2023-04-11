from django.urls import path
from .views import ProfileViewSet, CreateUserView, LoginView, CurrentUserView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('profiles/', ProfileViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('profiles/<int:pk>/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('users/create/', CreateUserView.as_view(), name='create_user'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/me/', CurrentUserView.as_view(), name='current_user'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

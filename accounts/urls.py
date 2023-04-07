from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, CreateUserView, CustomAuthToken, CurrentUserView

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/accounts/register/', CreateUserView.as_view()),
    path('api/accounts/login/', CustomAuthToken.as_view()),
    path('api/accounts/current/', CurrentUserView.as_view()),
]


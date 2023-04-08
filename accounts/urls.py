from django.urls import path, include
from rest_framework import routers
from .views import ProfileViewSet, CreateUserView, CustomAuthToken, CurrentUserView, LoginView

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/accounts/login/', LoginView.as_view(), name='login'),
    path('api/accounts/register-user/', CreateUserView.as_view()),
    path('api/accounts/current-user/', CurrentUserView.as_view()),
    path('api/accounts/token-auth/', CustomAuthToken.as_view()),
]

urlpatterns += router.urls
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from accounts.views import HomeRedirectView, CustomUserViewSet, ProfileViewSet
from accounts import views
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register(r'users', views.CustomUserViewSet)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileViewSet.as_view({'get': 'my_profile'}), name='profile'),
    path('signup/', CustomUserViewSet.as_view({'post': 'signup'}), name='signup'),
]

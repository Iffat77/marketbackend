from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from .views import SignupView, UserProfileView, UserLoginView
from django.views.generic import TemplateView


urlpatterns = [
    path('register/', SignupView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

# urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

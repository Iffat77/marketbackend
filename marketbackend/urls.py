from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView



urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # path('api_auth/', include('rest_framework.urls')),
    # path('profile/', include('user_profile.urls'))
]



urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]

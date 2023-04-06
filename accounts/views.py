from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CustomUserSerializer, ProfileSerializer
from .models import Profile, User

class CustomUserViewSet(viewsets.ModelViewSet):
    serializer_class = CustomUserSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        Profile.objects.create(user=user)

        return Response(serializer.data)

class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        profile = self.get_queryset().get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

from django.views.generic import RedirectView

class HomeRedirectView(RedirectView):
    url = '/'


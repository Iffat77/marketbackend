from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import permissions
from .models import Profile
from django.contrib import auth
from .serializers import ProfileSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

@method_decorator(csrf_protect, name='dispatch')
class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        password = data['password']
        re_password = data['re_password']
   
        try:
            if password == re_password:
                if User.objects.filter(username=username).exists():
                    return Response({"error": "Username already exists"})
                else:
                    if len(password) < 6:
                        return Response({"error": "Password must be at least 6 characters"})
                    else:
                        user = User.objects.create_user(
                            username=data['username'], password=data['password'])
                        user.save()
                        user_account = User.objects.get(id=user.id)
                        profile = Profile.objects.create(
                            user_id=user_account)
                        profile.save()

                        return Response({'success': 'User created successfully!'})
            else:
                return Response({'error': "Passwords do not match!"})
        except:
            return Response({'error': "Something went wrong signing you up!"})

class UserProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        profile = Profile.objects.get(user=self.request.user)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializers import UserSerializer
from user.models import User


class CustomTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            data = request.data
            user = get_object_or_404(User, username=data['username'])
            user_data = {
                'user_id': user.id,
                'username': user.username,
                'image': user.image.url
            }
            response.data['user'] = user_data

        return response


class RegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Registration successful", "code": 201}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

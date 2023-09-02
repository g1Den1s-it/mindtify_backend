from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from user.serializers import UserSerializer


class RegistrationView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        data['password'] = make_password(data['password'])

        serializer = UserSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "Registration successful", "code": 201}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

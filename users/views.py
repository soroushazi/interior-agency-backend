from django.shortcuts import render

from rest_framework import generics, status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


User = get_user_model()


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User registered successfully."
        }, status=status.HTTP_201_CREATED)

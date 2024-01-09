# myapp/views.py
from rest_framework import generics

from .models import User, UserConfiguration
from .serializers import UserSerializer, UserConfigurationSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserConfigurationListCreateView(generics.ListCreateAPIView):
    queryset = UserConfiguration.objects.all()
    serializer_class = UserConfigurationSerializer

class UserConfigurationRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserConfiguration.objects.all()
    serializer_class = UserConfigurationSerializer

# myapp/serializers.py
from rest_framework import serializers
from .models import User, UserConfiguration

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfiguration
        fields = '__all__'

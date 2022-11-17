from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
  password = serializers.CharField(max_length=65, min_length=8, write_only=True)
  email = serializers.EmailField(max_length=55, min_length=5)
  first_name = serializers.CharField(max_length=60, min_length=2)
  last_name = serializers.CharField(max_length=60, min_length=2)

  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']

  
  def validate_email(self, e):
    if User.objects.filter(email=e).exists():
      raise serializers.ValidationError('Email Already in use')
    return e

  def create(self, validated_data):
    return User.objects.create_user(**validated_data)
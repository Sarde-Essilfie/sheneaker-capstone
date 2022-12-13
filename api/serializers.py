from dataclasses import fields
from rest_framework import serializers
from sneaker_app.models import Sneaker
from django.contrib.auth import get_user_model

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model
        fields = ('__all__')
   
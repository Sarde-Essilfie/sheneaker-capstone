from dataclasses import fields
from rest_framework import serializers
from sneaker_app.models import Sneaker
from django.contrib.auth import get_user_model

class SneakerSerializer(serializers.ModelSerializer):
    # favorites = serializers.PrimaryKeyRelatedField(many=True, queryset=get_user_model().objects.all())
    class Meta:
        model = Sneaker
        fields = ('__all__')

class UserSerializer(serializers.ModelSerializer):
    favorites = SneakerSerializer(many=True, read_only=True)
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
            "favorites",
        )
   
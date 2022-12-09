from rest_framework import serializers
from sneaker_app.models import Sneaker

class SneakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sneaker
        fields = ('__all__')
from rest_framework import viewsets
from sneaker_app.models import Sneaker
from .serializers import SneakerSerializer

class SneakerViewSet(viewsets.ModelViewSet):
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer


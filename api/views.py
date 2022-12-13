from rest_framework import viewsets, generics
from sneaker_app.models import Sneaker
from .serializers import SneakerSerializer, UserSerializer
from django.contrib.auth import get_user_model

class SneakerViewSet(viewsets.ModelViewSet):
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user



from rest_framework.response import Response
from rest_framework import viewsets, generics, filters
from sneaker_app.models import Sneaker


# from sneaker_app.models import Sneaker
# class SneakerViewSet():
#     queryset = Sneaker.objects.all()

# from sneaker_app import models
# class SneakerViewSet():
#     queryset = models.Sneaker.objects.all()




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

# class GetBrands(viewsets.ModelViewSet):
#     serializer_class = SneakerSerializer
#     def list(self, request, *args, **kwargs):
#         brand = request.QUERY_DICT.get("brand")
#         data = self.get_queryset().filter(brand=brand)
#         serialized_data = self.get_serializer(data, many=True)
#         return Response(serialized_data.data)

class GetBrandsSearchView(generics.ListAPIView):
    queryset = Sneaker.objects.all()
    serializer_class = SneakerSerializer
    search_fields = ['brand']
    filter_backends = [
        filters.SearchFilter
    ]
    







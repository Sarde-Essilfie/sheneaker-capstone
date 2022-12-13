from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('sneakers', views.SneakerViewSet, basename='sneakers')

urlpatterns = router.urls + [
    path('currentuser/', views.CurrentUserView.as_view())
]
    



from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('sneakers', views.SneakerViewSet, basename='sneakers')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('currentuser/', views.CurrentUserView.as_view()),
    path('sneakers/brand/', views.GetBrandsSearchView.as_view()),
] + router.urls

    



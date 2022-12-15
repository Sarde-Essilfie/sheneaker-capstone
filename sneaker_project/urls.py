"""sneaker_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('admin/', admin.site.urls),
    path('admin/doc/', include('django.contrib.admindocs.urls')),

    path('users-app/', include('django.contrib.auth.urls')),
    path('users-app/', include('users_app.urls')),

    # path('sneaker-app/', include('sneaker_app.urls')),
    path('api/v1/', include('api.urls')),
   

]
    # sardes-awesome-sneakers.com/api/v1/
    # http://127.0.0.1:8000/api/v1/
    # http://localhost:8000/api/v1/
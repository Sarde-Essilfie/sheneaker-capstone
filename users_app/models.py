from django.contrib.auth.models import AbstractUser
from django.db import models
from sneaker_app.models import Sneaker

# Create your models here.


class CustomUser(AbstractUser):
    # favoriteSneakers = models.ManyToManyField(Sneaker, related_name="users")
    pass
    def __str__(self):
        return self.username


from django.db import models

# Create your models here.


class Sneaker(models.Model):
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    # image = models.URLf
    # links =
    # gender = models.CharField(max_length=200)

    def __str__(self):
        return self.name

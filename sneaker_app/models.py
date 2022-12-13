from django.db import models

# Create your models here.


class Sneaker(models.Model):
    # id = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    color = models.CharField(max_length=200, default='Not Available')
    price = models.IntegerField(default=0)
    # image = models.URLField(max_length=200, default='https://assets.adidas.com/images/h_840,f_auto,q_auto,fl_lossy,c_fill,g_auto/3cf0c669b07048cdb455ae02000e88df_9366/NMD_R1_Shoes_Pink_GZ4963_01_standard.jpg')
    image = models.JSONField(blank=True, null=True)
    links = models.URLField(max_length=200, default='https://stockx.com/nike-dunk-low-mineral-teal-gs')
    gender = models.CharField(max_length=200, default='N/A')


    def __str__(self):
        return self.name 

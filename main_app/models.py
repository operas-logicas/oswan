from django.db import models
from django.conf import settings

# Create your models here.
class Motorcycle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    horsePower = models.IntegerField()
    transStyle = models.CharField(max_length=50)
    engineStyle = models.CharField(max_length=50)
    engineCapacity = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    productImage = models.ImageField(upload_to='motorcycle_images', default='default.jpg')
    
    def __str__(self):
        return self.model

class Favorite(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favs = models.TextField(default='')
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

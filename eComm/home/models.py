from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=15)
    logo=models.ImageField(upload_to='itemPhoto')
    desc=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=3)
    cate=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name
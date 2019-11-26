from django.db import models

# Create your models here.
class Item(models.Model):
    productID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=15)
    logo=models.ImageField(upload_to='itemPhoto')
    desc=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=3)
    cate=models.CharField(max_length=15)
    gender=models.CharField(max_length=15)
    offer=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class User(models.Model):
    userID=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    firstName=models.CharField(max_length=15)
    lastName=models.CharField(max_length=15)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.firstName+self.lastName+str(self.userID)
    class meta:
        name='user info'
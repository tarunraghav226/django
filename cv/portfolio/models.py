from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    dob=models.DateField()
    mot_name=models.CharField(max_length=30)
    From=models.CharField(max_length=30)
    current=models.CharField(max_length=30)
    school=models.CharField(max_length=30)
    university=models.CharField(max_length=30)
    x=models.CharField(max_length=5)
    xii=models.CharField(max_length=5)
    hobbies=models.TextField()
    skills=models.TextField()
    desc=models.TextField()
    dp=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
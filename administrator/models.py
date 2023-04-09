from django.db import models
from django.apps import apps

# Create your models here.
class Student(models.Model):
    firstName =models.CharField(max_length=255)
    lastName =models.CharField(max_length=200) 
    registrtionNo =models.CharField(max_length =255)
    image =models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.firstName+" "+self.lastName
    

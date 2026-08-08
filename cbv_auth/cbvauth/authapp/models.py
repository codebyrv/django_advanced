from django.db import models
from django.contrib.auth.models import User# Create your models here.


class Student(models.Model):
    
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    course=models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.name
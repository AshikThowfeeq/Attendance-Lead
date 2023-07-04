from django.db import models
from django.utils import timezone

class Classroom(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Students(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    register_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    attendance = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
 

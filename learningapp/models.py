from django.db import models

# Create your models here.

class LearningCourses(models.Model):
    name=models.CharField(max_length=50)
    cat1=models.CharField(max_length=50)
    cat2=models.CharField(max_length=50)
    job_type=models.CharField(max_length=50)
    price=models.IntegerField()
    time=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
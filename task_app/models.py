from django.db import models

# Create your models here.
class Taskadd(models.Model):
    task = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
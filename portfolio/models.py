from django.db import models
from django.utils import timezone


class Project(models.Model):
    lenguaje = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)



class Certificaciones(models.Model):
    title = models.CharField(max_length=200)
    instituto = models.CharField(max_length=200)
    date = models.DateTimeField(timezone.now)
    certificacion = models.URLField(blank=True)
    description = models.TextField()
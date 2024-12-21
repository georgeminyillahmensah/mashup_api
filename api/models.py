from django.db import models

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=100)
    franchise = models.CharField(max_length=100)
    image = models.URLField()

class Quote(models.Model):
    text = models.TextField()
    source = models.CharField(max_length=100)

class Setting(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=100)

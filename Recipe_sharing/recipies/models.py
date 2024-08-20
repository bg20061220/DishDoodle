from django.db import models

# Create your models here.
class Recipe(models.Model):
    author = models.CharField(max_length=255)
    recipename  = models.CharField(max_length=255)
    majoringredients = models.TextField()
    recipe = models.TextField() 
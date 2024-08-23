from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes_posted')  # Rename to 'author'
    recipename  = models.CharField(max_length=255)
    majoringredients = models.TextField()
    recipe = models.TextField()

class SavedRecipes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_recipes')
    savedrecipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='saved_by_users')
    
    

from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    '''
        accepts name
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Ingredient(models.Model):
    '''
        accepts name, unit
    '''
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=63)

    def __str__(self):
        return f'{self.name}, {self.unit}'

class RecipeIngredient(models.Model):
    '''
        accepts recipe, ingredient, quantity
    '''
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.recipe}'

class Profile(models.Model):
    '''
        accepts a user, name, and bio
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=255)

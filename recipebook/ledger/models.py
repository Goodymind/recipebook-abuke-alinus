from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=63)

    def __str__(self):
        return f'{self.name}, {self.unit}'

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.recipe}'
from django.shortcuts import render
from .models import Recipe, RecipeIngredient

def recipe_list(request):
    '''
        list of recipes available
    '''
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request, 'recipe_list.html', context)

def recipe(request, id):
    '''
        for individual recipes
    '''
    recipe = Recipe.objects.get(id=id)
    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    context = {
        'recipe_ingredients': recipe_ingredients,
        'recipe': recipe,
    }

    return render(request, 'recipe_base.html', context)

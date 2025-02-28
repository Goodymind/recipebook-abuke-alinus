from django.shortcuts import render
from .models import Recipe, RecipeIngredient, Ingredient

def load_recipes():
    '''
        loads the recipes for use
    '''


def recipe_list(request):
    '''
        list of recipes available
    '''
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_list.html', context)

def recipe(request):
    '''
        for individual recipes
    '''

    load_recipes()
    recipes = CTX_RECIPES['recipes']
    for recipe in recipes:
        if recipe['link'] == request.path:
            return render(request, 'recipe_base.html', recipe)
    return render(request, 'invalid_page.html', recipe)

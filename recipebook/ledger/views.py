from django.shortcuts import render
from .recipes.recipe_parser import parse_recipes

CTX_RECIPES = {}
CTX_RECIPES_LOADED = False

def load_recipes():
    '''
        loads the recipes for use
    '''

    global CTX_RECIPES
    global CTX_RECIPES_LOADED
    if not CTX_RECIPES_LOADED:
        CTX_RECIPES = parse_recipes()
        CTX_RECIPES_LOADED = True

def get_recipe_list(request):
    '''
        list of recipes available
    '''

    load_recipes()
    return render(request, 'recipe_list.html', CTX_RECIPES)


def get_recipe(request):
    '''
        for individual recipes
    '''

    load_recipes()
    recipes = CTX_RECIPES['recipes']
    for recipe in recipes:
        if recipe['link'] == request.path:
            return render(request, 'recipe_base.html', recipe)
    return render(request, 'invalid_page.html', recipe)

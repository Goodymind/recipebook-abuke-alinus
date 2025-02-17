from django.shortcuts import render
from django.http import HttpResponse
from .recipes.recipe_parser import parse_recipes

ctx_recipes = {}
ctx_recipes_loaded = False

def index(request):
    return HttpResponse('index')

def load_recipes():
    global ctx_recipes
    global ctx_recipes_loaded
    if not ctx_recipes_loaded:
        ctx_recipes = parse_recipes()
        ctx_recipes_loaded = True

def get_recipe_list(request):
    load_recipes()
    return render(request, 'recipe_list.html', ctx_recipes)

def get_recipe(request):
    load_recipes()
    recipes = ctx_recipes['recipes']
    for recipe in recipes:
        if recipe['link'] == request.path:
            return render(request, 'recipe_base.html', recipe)
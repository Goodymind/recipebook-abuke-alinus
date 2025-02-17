from django.shortcuts import render
from django.http import HttpResponse
from .recipes.recipe_parser import parse_recipes

def index(request):
    return HttpResponse('index')

def get_recipe_list(request):
    return render(request, 'recipe_list.html', parse_recipes())
# Create your views here.

def get_recipe(request):

    return HttpResponse('recipe ' + request.method + request.path)
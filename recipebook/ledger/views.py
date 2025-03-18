from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient

@login_required
def recipe_list(request):
    '''
        list of recipes available
    '''
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }

    return render(request, 'recipe_list.html', context)

@login_required
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

def home(request):
    '''
        home page
    '''
    return render(request, 'home.html')

def root_redirect(request):
    '''
        redirect visitor to home page if not logged in and
        recipe-list if logged in.
    '''
    if request.user.is_authenticated:
        return redirect('recipe-list')
    
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredient, Profile

def __upload_recipe_image__(request, recipe):
    recipe_image = RecipeImage()
    recipe_image.recipe = recipe
    recipe_image.image = request.FILES.get('image')
    recipe_image.description = "alt text"
    recipe_image.save()

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

    if request.method == 'POST':
        __upload_recipe_image__(request, recipe)

    recipe_ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    recipe_images = RecipeImage.objects.filter(recipe=recipe)
    context = {
        'recipe_ingredients': recipe_ingredients,
        'recipe': recipe,
        'recipe_images': recipe_images,
    }

    return render(request, 'recipe_base.html', context)

@login_required
def recipe_upload(request):
    '''
        for uploading recipes
    '''
    if request.method == 'POST':
        recipe = Recipe()
        recipe.name = request.POST.get('recipe_name')
        recipe.author = Profile.objects.get(user=request.user)
        recipe.save()

        __upload_recipe_image__(request, recipe)

        ingredient_values = request.POST.getlist('ingredient')
        quantity_values = request.POST.getlist('quantity')
        unit_values = request.POST.getlist('unit')

        ingredient_list = []

        for ingredient_name, ingredient_unit in zip(ingredient_values, unit_values):
            try:
                ingredient = Ingredient.objects.get(name=ingredient_name, unit=ingredient_unit)
            except Ingredient.DoesNotExist:
                ingredient = Ingredient()
                ingredient.name = ingredient_name
                ingredient.unit = ingredient_unit
                ingredient.save()
            ingredient_list.append(ingredient)

        for ingredient, quantity in zip(ingredient_list, quantity_values):
            recipe_ingredient = RecipeIngredient()
            recipe_ingredient.recipe = recipe
            recipe_ingredient.ingredient = ingredient
            recipe_ingredient.quantity = quantity
            recipe_ingredient.save()

    return render(request, 'recipe_upload.html')

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

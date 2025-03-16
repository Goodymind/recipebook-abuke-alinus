from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile

class IngredientAdmin(admin.ModelAdmin):
    '''
        can filter by name as same ingredients can have different units
    '''
    model = Ingredient
    list_display = ('name', 'unit',)
    search_fields = ('name',)
    list_filter = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name', )
    search_fields = ('name', )

class RecipeIngredientAdmin(admin.ModelAdmin):
    '''
        can filter recipes from ingredients and vice versa
    '''
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity', )
    list_filter = ('recipe', 'ingredient', )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
admin.site.register(Profile)

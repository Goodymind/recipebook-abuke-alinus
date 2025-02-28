from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient

# Register your models here.
class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name', 'unit',)
    search_fields = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name', )
    search_fields = ('name', )

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity', )
    list_filter = ('recipe', 'ingredient', )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)
from django.urls import path

from . import views
urlpatterns=[
    path('recipes/list', views.recipe_list, name="recipe-list-name"),
    path('recipe/<int:id>', views.recipe, name="recipe-name"),
]

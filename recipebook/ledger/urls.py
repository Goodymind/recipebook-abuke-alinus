from django.urls import path

from . import views
urlpatterns=[
    # path('', views.index),
    path('', views.get_recipe_list, name="recipe-list-name"),
    path('recipe/1', views.get_recipe, name="recipe-1-name"),
    path('recipe/2', views.get_recipe, name="recipe-2-name")
]

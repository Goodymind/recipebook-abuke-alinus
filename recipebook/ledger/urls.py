from django.urls import path

from . import views
urlpatterns=[
    path('', views.index),
    path('recipelist', views.get_recipe_list, name="recipe-list-name")
]
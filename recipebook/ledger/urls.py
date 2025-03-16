from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
urlpatterns=[
    path('recipes/list', views.recipe_list, name="recipe-list"),
    path('recipe/<int:id>', views.recipe, name="recipe"),
    path('home', views.home, name='home'),
    path('', views.root_redirect, name='root_redirect'),
]

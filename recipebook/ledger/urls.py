from django.urls import path
from django.contrib.auth.views import LoginView

from . import views
urlpatterns=[
    path('recipes/list', views.recipe_list, name="recipe-list-name"),
    path('recipe/<int:id>', views.recipe, name="recipe-name"),
    path('', views.root_redirect, name='root_redirect'),
    # path('login/', LoginView, name='login')
]

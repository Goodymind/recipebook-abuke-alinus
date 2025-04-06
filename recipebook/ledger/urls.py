from django.urls import path

from . import views
urlpatterns=[
    path('recipes/list', views.recipe_list, name="recipe-list"),
    path('recipe/<int:id>', views.recipe, name="recipe"),
    path('recipe/add', views.recipe_upload, name='upload'),
    path('recipe/<int:pk>/add_image', views.recipe_image_upload, name="upload-image"),
    path('home', views.home, name='home'),
    path('', views.root_redirect, name='root_redirect'),
]

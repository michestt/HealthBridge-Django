from django.urls import path
from recipe.views import food_recipe,food_specific,add_recipe

urlpatterns = [
    path('',food_recipe,name='food_recipe'),
    path('food/<int:food_id>/',food_specific,name='food'),
    path('add_recipes/',add_recipe,name='add_recipe'),

]

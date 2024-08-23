from django.urls import path
from . import views

urlpatterns = [
    path('addrecipies/', views.addrecipies, name='addrecipies'),
    path('home/'  , views.home , name = 'home'),
    path('viewrecipies/' , views.viewrecipies , name = 'viewrecipies'),
    path('recipedetails/<int:id>' , views.recipedetails , name = 'recipedetails'),
    path('' , views.signin , name='signin'),
    path('logout/' , views.logout_view , name='logout'),
    path('postedrecipies/' , views.postedrecipies, name = 'postedrecipies'),
    path('savedrecipies/' , views.savedrecipies , name = 'savedrecipies'),
    path('saverecipe/<int:id>/', views.save_recipe, name='saverecipe'),
]
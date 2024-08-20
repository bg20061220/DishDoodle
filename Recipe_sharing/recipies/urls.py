from django.urls import path
from . import views

urlpatterns = [
    path('addrecipies/', views.addrecipies, name='addrecipies'),
    path(''  , views.home , name = 'home'),
    path('viewrecipies/' , views.viewrecipies , name = 'viewrecipies'),
    path('recipedetails/<int:id>' , views.recipedetails , name = 'recipedetails/id')
]
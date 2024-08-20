from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import RecipeForm 
from .models import Recipe

def addrecipies(request):
    if request.method == "POST":
       form = RecipeForm(request.POST)
       if form.is_valid():
          author = form.cleaned_data['author']
          recipename = form.cleaned_data['recipename']
          majoringredients = form.cleaned_data['majoringredients']
          recipe = form.cleaned_data['recipe']
          new_recipe = Recipe(author = author , recipename  = recipename , majoringredients = majoringredients , recipe = recipe)
          new_recipe.save()
          template = loader.get_template('main.html')
          return HttpResponse(template.render())
    else :
       form = RecipeForm()
       return render(request , "addrecipies.html" , {"form" : form})
     
def home(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def viewrecipies(request):
     recipies = Recipe.objects.all()
     return render(request , "viewrecipies.html" ,{'recipies' : recipies} )

def recipedetails(request , id):
   recipedetails = Recipe.objects.get(id = id )
   context = {
      "recipedetails" : recipedetails , 
    }
   return render(request, "recipedetails.html", context)
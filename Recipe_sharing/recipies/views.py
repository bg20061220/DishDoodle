from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RecipeForm 
from .models import Recipe
from django.contrib.auth import logout
from django.contrib.auth.models import User 
from .models import SavedRecipes
from django.shortcuts import render, get_object_or_404


def addrecipies(request):
   if request.user.is_authenticated:
        if request.method == "POST":
            form = RecipeForm(request.POST)
            if form.is_valid():
               
                author = request.user 
                recipename = form.cleaned_data['recipename']
                majoringredients = form.cleaned_data['majoringredients']
                recipe = form.cleaned_data['recipe']
                new_recipe = Recipe(author=author, recipename=recipename, majoringredients=majoringredients, recipe=recipe)
                new_recipe.save()
                return render(request , 'main.html')  # Redirect to a URL pattern, e.g., 'home'
        else:
            form = RecipeForm()
        return render(request, "addrecipies.html", {"form": form})
   return render(request , 'viewrecipies.html')
     
def home(request):
  context = {
            'user' : request.user  # Pass the user to the template if needed
    }
  return render(request, 'main.html', context)

def viewrecipies(request):
     recipies = Recipe.objects.all()
     return render(request , "viewrecipies.html" ,{'recipies' : recipies} )

def recipedetails(request , id):
   recipedetails = Recipe.objects.get(id = id )
   context = {
      "recipedetails" : recipedetails , 
    }
   return render(request, "recipedetails.html", context)

def signin(request):
   return render(request , 'signin.html')

def logout_view(request):
   logout(request)
   # user.is_active = False 
   return render(request , 'main.html')

def postedrecipies(request): 
     user = User.objects.get(username = request.user.username)
     postedrecipies = Recipe.objects.filter(author = user )
     context = {
         'postedrecipies' : postedrecipies
     }
     return render(request , 'postedrecipies.html' , context)


def save_recipe(request , id ):
    user = request.user 
    recipe = Recipe.objects.get(id = id )
    saved_recipe, created = SavedRecipes.objects.get_or_create(user=user, savedrecipe=recipe)
    
    
    return redirect('savedrecipies')

def savedrecipies (request ): 
    user = request.user 
    saved_recipies = SavedRecipes.objects.filter(user = user )
    recipe_details= []
    for saved in saved_recipies:
        recipe = get_object_or_404(Recipe , id = saved.savedrecipe.id)
        recipe_details.append(recipe )

    context = {
        'recipe_details' : recipe_details
    }    
    return render(request , 'savedrecipies.html' , context  )

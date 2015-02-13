from django.shortcuts import render

from recipeinfo.models import Recipe

# Create your views here.

def index(request):
    recipes=Recipe.objects.order_by('?')[:1]
    #recipes=Recipe.objects.all()
    return render(request, 'pi_main/index.html',{
        'recipes': recipes,
        })   

def about(request):
    return render(request, 'pi_main/about.html')

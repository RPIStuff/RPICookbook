from django.shortcuts import render

from recipeinfo.models import Recipe

# Create your views here.

def recipe_index(request):
    recipes=Recipe.objects.all()
    return render(request, 'recipeinfo/recipe_index.html', {
        'recipes': recipes,
        })
        
def recipe_detail(request, slug):
    recipe=Recipe.objects.get(slug=slug)
    return render(request, 'recipeinfo/recipe_detail.html', {
        'recipe': recipe,
        })
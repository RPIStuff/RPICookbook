from django.contrib import admin
from recipeinfo.models import Recipe
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class RecipeAdmin(SummernoteModelAdmin):
    fieldsets = [
        ('Recipe Details', {'fields': ['title', 'ingredients','method', 'sugarlevel',]}),
    ]
    
    list_display = ('title',)
    
class Media:
	js = [
		'/root/recipes/env/pi_proj/project/static/grapelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
		'/root/recipes/env/pi_proj/project/static/grapelli/tinymce_setup/tinymce_setup.js',
	]    
    
admin.site.register(Recipe, RecipeAdmin)

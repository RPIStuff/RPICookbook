from django.conf.urls import patterns, url

#from recipeinfo import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    url(r'^$', 'recipeinfo.views.recipe_index', name='recipe_index'),
)
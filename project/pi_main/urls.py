from django.conf.urls import patterns, include, url
from django.contrib import admin

from pi_main import views
from recipeinfo import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pi_main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^summernote/', include('django_summernote.urls')),    
    url(r'^$', 'pi_main.views.index', name='index'),
    url(r'^about/', 'pi_main.views.about', name='about'),
    
    url(r'^recipes/', include('recipeinfo.urls', namespace="recipes")),
    url(r'^recipe/(?P<slug>.+)/', 'recipeinfo.views.recipe_detail'),
    
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

from django.db import models
import datetime
from django.template.defaultfilters import slugify
from filebrowser.fields import FileBrowseField

# Create your models here.

SUGARLEVEL_CHOICES = (
    ('l', 'Low'),
    ('m', 'Medium'),
    ('h', 'High'),
)

class Recipe(models.Model):
    title=models.CharField(max_length=70)
    slug=models.SlugField(max_length=100, unique=True, null=True, blank=True, default=None)
    created=models.DateTimeField('Date created', auto_now_add=True)
    edited=models.DateTimeField('Last date edited', auto_now=True)
    featuredimage=FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg", ".png", ".gif"], blank=True, null=True, help_text="This is the featured image.")
    ingredients=models.TextField(null=True, blank=True, default=None)
    method=models.TextField(null=True, blank=True, default=None)
    sugarlevel = models.CharField(max_length=1, choices=SUGARLEVEL_CHOICES, default="l")
    metatitle=models.CharField(max_length=120, null=True, blank=True, default=None)
    metadescription=models.TextField(null=True, blank=True, default=None)
    metakeywords=models.CharField(max_length=500, null=True, blank=True, default=None)
    promoted=models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # Blank slug so set it
            self.slug = slugify(self.title)
            
        if not self.metatitle:
            self.metatitle=self.title
            
        super(Recipe, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.title

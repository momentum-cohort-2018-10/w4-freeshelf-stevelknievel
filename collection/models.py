from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    url = models.Charfield()
    slug = models.SlugField(unique=True)
    # date_added = models.DateTime??   need to figure this one out


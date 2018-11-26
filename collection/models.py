from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    slug = models.SlugField(unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    

class Category(models.Model):
    category = models.CharField(max_length=30)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


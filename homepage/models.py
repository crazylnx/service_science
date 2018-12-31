from django.db import models

# Create your models here.
class Category( models.Model):
    category_name = models.CharField(max_length=20)
    category_path = models.CharField(max_length=30)
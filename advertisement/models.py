from django.db import models

# Create your models here.
class ad(models.Model):
    ad_name=models.CharField(max_length=100)
    ad_path=models.CharField(max_length=1000)
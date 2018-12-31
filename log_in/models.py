from django.db import models
# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=8)
    user_password = models.CharField(max_length=10)
    user_money = models.IntegerField(default=0)
    user_image = models.CharField(default="", max_length=200)
    user_nickname = models.CharField(max_length=6)
    def __str__(self):
        return self.user_name

from django.db import models
# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=8)
    user_password = models.CharField(max_length=10)
    user_money = models.IntegerField(default=0)
    user_image = models.FileField(upload_to='static\\img\\photo\\%Y\\%m\\%d', default='static\\img\\photo\\facebook.png')
    def __str__(self):
        return self.user_name

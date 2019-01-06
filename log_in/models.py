from django.db import models
# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=1000)
    user_money = models.IntegerField(default=0)
    user_image = models.FileField(upload_to='static\\img\\photo\\%Y\\%m\\%d', default='static\\img\\photo\\facebook.png')
    signature = models.CharField(default="这个人很懒，什么都没留下",max_length=2000)
    gender = models.CharField(default='女',max_length=5)

    def __str__(self):
        return self.user_name

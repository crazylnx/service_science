from django.db import models

# Create your models here.
class reward(models.Model):
    reward_user_id1=models.ForeignKey('log_in.user',related_name='payuser', on_delete=models.CASCADE)
    reward_user_id2=models.ForeignKey('log_in.user',related_name='getpayuser', on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
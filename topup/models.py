from django.db import models

# Create your models here.
class topup(models.Model):
    topup_date=models.DateTimeField(auto_now_add=True)
    topup_user_id=models.ForeignKey('log_in.user',on_delete=models.CASCADE)
    topup_amount=models.IntegerField(default=0)
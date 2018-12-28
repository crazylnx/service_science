from django.db import models

# Create your models here.
class history(models.Model):
    history_user_id=models.ForeignKey('log_in.user',on_delete=models.CASCADE)
    history_question_id=models.ForeignKey('my_comments.question',on_delete=models.CASCADE)
    history_date=models.DateTimeField('date published')
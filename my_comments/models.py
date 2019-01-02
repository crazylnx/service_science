from django.db import models

# Create your models here.
class question(models.Model):
    question_user_id=models.ForeignKey('log_in.user',on_delete=models.CASCADE)
    question_type=models.CharField(max_length=10)
    question_date=models.DateTimeField('date published')
    question_name=models.CharField(max_length=100)
    question_content=models.CharField(max_length=10000)
    def __str__(self):
        return question.question_type
class comment(models.Model):
    comment_question_id=models.ForeignKey(question,on_delete=models.CASCADE)
    comment_date=models.DateTimeField('date published')
    comment_content=models.CharField(max_length=5000)

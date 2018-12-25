from django.db import models
import django.utils.timezone as timezone
from django.utils.html import format_html


# Create your models here.
class User(models.Model):
    UserName = models.CharField(max_length=64, primary_key=True)
    passward = models.CharField(max_length=64, null=False)
    status = models.CharField(max_length=64, default="user")
    signupTime = models.DateTimeField('注册时间', default=timezone.now)
    country = models.CharField(max_length=64, default='')
    province = models.CharField(max_length=64, default='')
    city = models.CharField(max_length=64, default='')
    sex = models.CharField(max_length=10, default='')
    pic_height = models.IntegerField(default=100)
    pic_width = models.IntegerField(default=100)
    pic_url = models.ImageField(upload_to="头像", height_field='pic_height', width_field='pic_width', max_length=255)
    following_num = models.IntegerField(default=0)
    follower_num = models.IntegerField(default=0)
    question_num = models.IntegerField(default=0)
    answer_num = models.IntegerField(default=0)
    balance = models.DecimalField(decimal_places=2, max_digits=10)
    phoneNum = models.CharField(max_length=14, default='')

    def image_data(self):
        return format_html('<img scr="{}" width="100px"/>', self.pic_url.url)


class Question(models.Model):
    QuestionID = models.CharField(max_length=64, primary_key=True)
    QuestionText = models.CharField(max_length=500, null=False)
    AskerName = models.ForeignKey(User, related_name='Question_AskerName', on_delete=models.CASCADE, default='')
    type = models.CharField(max_length=64, default='')
    follower_num = models.IntegerField(default=0)
    answer_num = models.IntegerField(default=0)
    askTime = models.DateTimeField('提问时间', default=timezone.now)


class Answer(models.Model):
    AnswerID = models.CharField(max_length=64, primary_key=True)
    AnswerText = models.CharField(max_length=500, null=False)
    QuestionID = models.ForeignKey(Question, related_name='Answer_QuestionID', on_delete=models.CASCADE, null=False)
    AnswererName = models.ForeignKey(User, related_name='Answer_AnswererName', on_delete=models.CASCADE, default='')
    AnswerTime = models.DateTimeField('回答时间', default=timezone.now)
    like_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)


class Comment(models.Model):
    CommentID = models.CharField(max_length=64, primary_key=True)
    AnswerId = models.ForeignKey(Answer, related_name='Comment_AnswerID', on_delete=models.CASCADE, null=False)
    UserName = models.ForeignKey(User, related_name='Comment_UserName', on_delete=models.CASCADE, default='')
    commentText = models.CharField(max_length=500, null=False)
    commentTime = models.DateTimeField("评论时间", default=timezone.now)


class Follow(models.Model):
    UserName = models.ForeignKey(User, related_name='Follow_UserName', on_delete=models.CASCADE, null=False)
    FollowerName = models.ForeignKey(User, related_name='Follow_FollowerName', on_delete=models.CASCADE, null=False)
    FollowTime = models.DateTimeField("关注时间", default=timezone.now)


class Browse(models.Model):
    UserName = models.ForeignKey(User, related_name='Browse_UserName', on_delete=models.CASCADE, null=False)
    QuestionID = models.ForeignKey(Question, related_name='Browse_QuestionID', on_delete=models.CASCADE, null=False)
    AnswerID = models.ForeignKey(Answer, related_name='Browse_AnswerID', on_delete=models.CASCADE, null=False)
    BrowseTime = models.DateTimeField(default=timezone.now)

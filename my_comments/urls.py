from django.urls import path
from my_comments.views import *
from django.conf import settings
app_name='my_comments'
urlpatterns = [
    path('MyComment/', MyComments, name='mycomments'),
    path('MyComment/Inner', MyCommentsInner, name='mycommentsinner'),
    path('/homepage/question/<int:questionId>',ShowQuestion,name='showquestion')
]
from django.urls import path
from show_question.views import *
from django.conf import settings
app_name = 'show_question'
urlpatterns = [
    path('ShowQuestion/', ShowQuestion, name='showquestion'),
    # path()
]
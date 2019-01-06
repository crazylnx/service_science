import datetime

from django.shortcuts import render, redirect

# Create your views here.
from my_browsing_history.models import *
from  log_in.models import *
def MyBrowsingHistory(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    elif request.method == 'POST':
        pass
    else:
        userName = request.session.get('userName')
        context = {}
        try:
            aUser = user.objects.get(user_name=userName)
            context.update(imagePath=aUser.user_image.url)
            context.update(username=aUser.user_name)
            return render(request, 'my_browsing_history/IBrowsed.html',context)
        except:
            return render(request, 'my_browsing_history/IBrowsed.html', context)
class histroyshow(object):
    def __init__(self,date='',question_name='',question_id=0):
        self.date=date
        self.question_name=question_name
        self.question_id=question_id
def MyBrowsingHistoryInner(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    username = request.session.get('userName')
    try:

        aUser = user.objects.get(user_name=username)
        historylist = aUser.history_set.order_by('-id')
        questionlist=[]
        for ahistory in historylist:
            question1 = ahistory.history_question_id
            a1 = histroyshow()
            a1.date= ahistory.history_date
            a1.question_name=question1.question_name
            a1.question_id=question1.pk
            questionlist.append(a1)
        context = {}
        context.update(username=username)
        context.update(questionlist=questionlist)
        return render(request,'my_browsing_history/inner_IBrowsed.html',context)
    except user.DoesNotExist:
        return redirect('login')




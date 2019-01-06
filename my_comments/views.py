import datetime

from django.shortcuts import render, redirect

# Create your views here.
from my_comments.models import *
from my_comments.form import *
from  log_in.models import *
from my_browsing_history.models import *
def MyComments(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    elif request.method == 'POST':
        pass
    else:
        return render(request, 'my_comments/MyComments.html')

def MyCommentsInner(request):
    return render(request, 'my_comments/inner_MyComments.html')

def ShowQuestion(request,questionId):
    if not request.session.has_key('userName'):
        return redirect('login')
    else:
        userName = request.session.get('userName')
        try:
            aUser = user.objects.get(user_name=userName)
            print (aUser)
            if request.method == 'POST':
                Form = CommentForm(request.POST)
                if Form.is_valid():
                    data = Form.cleaned_data
                    print(data)
                    acomment = comment(comment_question_id_id=questionId, comment_date=datetime.datetime.now(),
                                       comment_content=data['comment'],comment_user=aUser)
                    acomment.save()
                    try:
                        aQuestion = question.objects.get(pk=questionId)
                        context = {}
                        context.update(question=aQuestion)
                        context.update(commentCount=aQuestion.comment_set.count())
                        try:
                            form = CommentForm(request.POST)
                            context.update(form=form)
                            commentList = aQuestion.comment_set.all()
                            context.update(commentList=commentList)
                            return render(request, 'show_question/article_single.html', context)
                        except question.DoesNotExist:
                            context.update(commentList='')
                            return render(request, 'show_question/article_single.html', context)
                    except question.DoesNotExist:
                        context = {}
                        form = CommentForm()
                        context.update(form=form)
                        context.update(question='')
                        context.update(commentCount='')
                        context.update(commentList='')
                        return render(request, 'show_question/article_single.html', context)
            else:
                try:
                    aQuestion = question.objects.get(pk=questionId)
                    context = {}
                    context.update(question=aQuestion)
                    context.update(commentCount=aQuestion.comment_set.count())
                    try:
                        form = CommentForm()
                        context.update(form=form)
                        commentList = aQuestion.comment_set.all()
                        aHistory = history(history_date=datetime.datetime.now(),history_question_id=aQuestion, history_user_id=aUser)
                        aHistory.save()
                        context.update(commentList=commentList)
                        return render(request, 'show_question/article_single.html', context)
                    except comment.DoesNotExist:
                        form = CommentForm()
                        context.update(form=form)
                        context.update(commentList='')
                        return render(request, 'show_question/article_single.html', context)
                except question.DoesNotExist:
                    context = {}
                    form = CommentForm()
                    context.update(form=form)
                    context.update(question='')
                    context.update(commentCount='')
                    context.update(commentList='')
                    return render(request, 'show_question/article_single.html', context)
        except user.DoesNotExist:
            return redirect('login')

def RaiseQuestion(request):

    if not request.session.has_key('userName'):
        return redirect('login')
    aUsername = request.session.get('userName')
    try:
        aUser = user.objects.get(user_name=aUsername)
        context = {}
        if (request.method == 'POST'):
            form = QuestionForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                aQuestion = question()
                aQuestion.question_name=data['question']
                aQuestion.question_content = data['detail']
                aQuestion.question_date=datetime.datetime.now()
                aQuestion.question_user_id=aUser
                aQuestion.save()

                return redirect('homepage1:homepageinner')
        form = QuestionForm()
        context.update(form=form)
        return render(request, 'my_comments/RaiseQuestion.html', context)
    except user.DoesNotExist:
        return redirect('login')

def MyQuestion(request):
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
            return render(request, 'my_comments/MyQuestion.html', context)
        except:
            return render(request, 'my_comments/MyQuestion.html', context)
class myquestionshow(object):
    def __init__(self,date='',question_name='',question_content='',question_id=0):
        self.date=date
        self.question_name=question_name
        self.question_content=question_content
        self.question_id=question_id
def MyQuestionInner(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    username = request.session.get('userName')
    try:
        aUser = user.objects.get(user_name=username)
        questions = aUser.question_set.order_by('-question_date')
        questionlist=[]
        for aquestion in questions:
            question1 = aquestion.pk
            a1 = myquestionshow()
            a1.date= aquestion.question_date
            a1.question_name=aquestion.question_name
            a1.question_content=aquestion.question_content
            a1.question_id=question1
            questionlist.append(a1)
        context = {}
        context.update(username=username)
        context.update(questionlist=questionlist)
        return render(request,'my_comments/inner_MyQuestion.html',context)
    except user.DoesNotExist:
        return redirect('login')


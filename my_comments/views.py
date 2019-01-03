import datetime

from django.shortcuts import render, redirect
from my_comments.models import *
from my_comments.form import *
from  log_in.models import *
# Create your views here.
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


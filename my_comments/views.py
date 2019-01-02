from django.shortcuts import render, redirect
from my_comments.models import *

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

# def ShowQuestion(request,questionId):
#     if not request.session.has_key('userName'):
#         return redirect('login')
#     elif request.method == 'POST':
#         pass
#     else:
#         try:
#             aQuestion = question.objects.get(pk=questionId)
#             context = {}
#             context.update(question=aQuestion)
#             context.update(commentCount=aQuestion.comment_set.count())
#             return render(request, 'show_question/article_single.html', question)
#         except question.DoesNotExist:
#             return render()

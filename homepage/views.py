from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
# Create your views here.
from homepage.models import Category
from log_in.models import *
from log_in.forms import LoginForm
from log_in.urls import *
from my_comments.models import *

def homepage_view(request):
    if not request.session.has_key('userName'):
        form = LoginForm()
        return HttpResponseRedirect('/')
    else:
        userName = request.session.get('userName')
        print(userName)
        aUser = user.objects.get(user_name=userName)
        aCategory = Category.objects.all()
        context = {}
        context.update(imagePath=aUser.user_image)
        context.update(username=aUser.user_nickname)
        context.update(categories=aCategory)
        return render(request, 'homepage/Homepage.html', context)
def HomepageInner(request):
    try:
        questionlist = question.objects.all()
        context = {}
        # for foo in questionlist:
        #     context.update(=foo.comment_set.count())
        context.update(questionlist=questionlist)
        # context={}
        # context.update(questionlist=questionlist)
        # a = questionlist[0].comment_set.count()
        # print(a)
        # for foo in questionlist:
        #     commentCount = foo.comment_set.count()
        #    context.update(commentCount, commentCount)
        return render(request, 'homepage/inner_Homepage.html', context)
        # return HttpResponse("nnnn")
    except question.DoesNotExist:
        context = {}
        return render(request, 'homepage/inner_Homepage.html', context)
        # return HttpResponse("nnnn")


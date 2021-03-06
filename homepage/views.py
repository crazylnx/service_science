from itertools import count

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.db.models import Count
# Create your views here.
from log_in.models import *
from log_in.forms import LoginForm
from log_in.urls import *
from my_comments.models import *
from .forms import *
def homepage_view(request):
    if not request.session.has_key('userName'):
        form = LoginForm()
        return HttpResponseRedirect('/')
    else:
        userName = request.session.get('userName')
        print(userName)
        try:
            aUser = user.objects.get(user_name=userName)
            try:
                questionRecommendList = question.objects.annotate(num1=Count('comment')).order_by('-num1')
                # print(questionRecommendList[0].question_name)
                context = {}
                context.update(imagePath=aUser.user_image.url)
                context.update(username=aUser.user_name)
                context.update(categories=questionRecommendList)

                commentcount = aUser.comment_set.count()
                context.update(money=aUser.user_money)
                context.update(commentcount=commentcount)
                return render(request, 'homepage/Homepage.html', context)
            except question.DoesNotExist:
                context = {}
                context.update(categories='')
                context.update(imagePath=aUser.user_image)
                context.update(username=aUser.user_name)
                return render(request, 'homepage/Homepage.html', context)
        except user.DoesNotExist:
            return HttpResponseRedirect('login')
def HomepageInner(request):
    try:
        questionlist = question.objects.order_by('-question_date')
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
        form = SearchForm()
        context.update(form=form)
        context.update(display1=False)
        return render(request, 'homepage/inner_Homepage.html', context)
        # return HttpResponse("nnnn")
    except question.DoesNotExist:
        context = {}
        return render(request, 'homepage/inner_Homepage.html', context)
        # return HttpResponse("nnnn")

def Search(request):
    context = {}
    # print("进入search")
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            questionlist = question.objects.filter(question_name__icontains=data['KeyWord']).order_by('-question_date')
            context.update(questionlist=questionlist)
            form = SearchForm()
            context.update(form = form)
            print(request.POST.get('hide'))
            if request.POST.get('hide') == '1':
                context.update(display1=True)
            else:
                context.update(display1=False)
            print(context.get('display1'))
            return render(request, 'homepage/inner_Homepage.html', context)
    form = SearchForm()
    context.update(form=form)
    return render(request, "homepage/inner_Homepage.html", context)

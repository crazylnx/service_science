from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from homepage.models import Category
from log_in.models import *
from log_in.forms import LoginForm
from log_in.urls import *

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

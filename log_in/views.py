import base64

from django.core.files import File
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files import images
# Create your views here.
from log_in.models import *
from log_in.forms import *
from homepage.forms import SearchForm
from homepage.models import *
from log_in.models import user



#注册界面
def register_view(request):
    context={}
    if request.method == 'POST':
        img = request.FILES.get('img')
        name = request.FILES.get('img').name
        new_user=user(user_name='a',user_password='123456',user_image=img,user_nickname='kitty')
        new_user.save()
        context.update(user1=new_user)
        print(name)
        return render(request,'log_in/register.html',context)
    else:
        context.update(user='')
        return render(request,'log_in/register.html',context)

# 登陆页面，获取request的username和password，成功到Homepage.html,失败返回原来界面，并带参数data显示error
@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['password'])
            try:
                aUser = user.objects.get(user_name=data['username'], user_password=data['password'])
                request.session['userName'] = aUser.user_name
                request.session.set_expiry(0)
                #return HttpResponseRedirect('homepage/')
                return redirect('homepage1:homepage')
            except user.DoesNotExist:
                form = LoginForm()
                return render(request, 'log_in/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'log_in/login.html', {'form': form})




def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'log_in/signup.html', {'form':form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print(data['username'])
            newUser = user()
            newUser.user_name = data['username']
            newUser.user_password = data['password1']
            newUser.save()
            return redirect('login')
        return render(request, 'log_in/signup.html', {'form':form})

def ChangeInfo(request):
    if not request.session.has_key('userName'):
        return  redirect('login')
    userName = request.session.get('userName')
    print(userName)
    if request.method == 'POST':
        try:
            aUser = user.objects.get(user_name=userName)
            aUser.signature=request.POST.get('signature')
            aUser.gender=request.POST.get('gender')
            aUser.user_image=request.POST.get('img')
            aUser.save()
            return render(request, 'log_in/Change_Personal_Info.html', {"aUser": aUser})
        except user.DoesNotExist:
            return redirect('login')
    else:
        try:
            aUser = user.objects.get(user_name=userName)
            return render(request, 'log_in/Change_Personal_Info.html', {"aUser": aUser})
        except user.DoesNotExist:
            return redirect('login')










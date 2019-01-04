import base64

from django.core.files import File
from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files import images
# Create your views here.
from log_in.models import *
from log_in.forms import LoginForm

from homepage.models import *



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
                return HttpResponseRedirect('homepage/')
            except user.DoesNotExist:
                form = LoginForm()
                return render(request, 'log_in/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'log_in/login.html', {'form': form})




def register(request):
    data = request.get_json()
    print(data)
    newUser = user()
    if request.POST.get('user_name').strip():
        newUser.user_name = request.POST.get('user_name').strip()
    if request.POST.get('user_password').strip():
        newUser.user_password = request.POST.get('user_password').strip()
    if request.POST.get('user_money').strip():
        newUser.user_money = request.POST.get('user_money').strip()
    if request.POST.get('user_image').strip():
        newUser.user_image = request.POST.get('user_image').strip()
    if request.POST.get('user_nickname').strip():
        newUser.user_nickname = request.POST.get('user_nickname').strip()
    user.save()







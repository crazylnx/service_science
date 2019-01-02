import base64

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from log_in.models import *
from log_in.forms import LoginForm
from homepage.models import *



#注册界面@todo
def register_view(request):
    pass

# 登陆页面，获取request的username和password，成功到Homepage.html,失败返回原来界面，并带参数data显示error
@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            aCategory = Category.objects.all()
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







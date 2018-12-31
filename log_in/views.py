from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from log_in.models import *
from homepage.models import *

# 登陆界面
def login_view(request):
    return render(request,'login.html')

#注册界面@todo
def register_view(request):
    pass

# 登陆检测，获取request的username和password，成功到Homepage.html,失败返回原来界面，并带参数data显示error
@csrf_exempt
def login(request):
    name = request.POST.get('username')
    password = request.POST.get('password')
    try:
        aUser = user.objects.get(user_name=name, user_password=password)
        aCategory=Category.objects.all()
        context = {}
        context.update(imagePath=aUser.user_image)
        context.update(username=aUser.user_nickname)
        context.update(categories=aCategory)
        return render(request,'Homepage.html',context)
    except user.DoesNotExist:
        return redirect('login')

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







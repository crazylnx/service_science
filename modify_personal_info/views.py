from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
# Create your views here.
from log_in.models import *
def personal_view(request, name):
    context = {}
    try:
        userlist = user.objects.get(user_name=name)
        context.update(foo=userlist)
        print(context)
        return render(request, 'my_reward/reward.html', context)
    except user.DoesNotExist:
        return redirect('homepage1:homepage')

def Reward(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    giver_name = request.session.get('userName')
    taker_name = request.POST.get('takername')
    giver = user.objects.get(user_name=giver_name)
    taker = user.objects.get(user_name=taker_name)

    if request.POST.get('recharge'):
        value = int(request.POST.get('recharge'))
        if giver.user_money - value >= 0:
            giver.user_money = giver.user_money - value
            taker.user_money = taker.user_money + value
            giver.save()
            taker.save()
            messages.success(request, "打赏成功")
        else:
            messages.error(request, "余额不足")
    else:
        messages.warning(request, "未选择充值金额")

    return render(request, 'my_reward/reward.html', {"foo": taker})

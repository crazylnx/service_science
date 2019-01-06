from django.shortcuts import render, redirect
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

def reward(request, name, value):
    if not request.session.has_key('userName'):
        return redirect('login')
    giver_name = request.session.get('userName')
    print(giver_name)
    giver = user.objects.get(user_name=giver_name)
    taker = user.objects.get(user_name=name)
    if giver.user_money - value >= 0:
        giver.user_money = giver.user_money - value
        taker.user_money = taker.user_money + value
        giver.save()
        taker.save()
    return render(request, 'my_reward/reward.html',{"foo":taker})

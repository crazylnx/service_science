from django.shortcuts import render, redirect

# Create your views here.
from log_in.models import user
def popup(request):
    userName = request.session.get('userName')
    if request.method == 'POST':
        try:
            aUser = user.objects.get(user_name= userName)
            if request.POST.get("recharge"):
                user_money = int(request.POST.get("recharge"))
                aUser.user_money = aUser.user_money + user_money
                aUser.save()
            return render(request, "my_reward/recharge_response.html")
        except user.DoesNotExist:
            return redirect('login')
    else:
        return render(request,'my_reward/rechargepopup.html')

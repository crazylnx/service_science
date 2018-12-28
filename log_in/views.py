from django.shortcuts import render

# Create your views here.
def login(request):
    name=request.POST.get("username")
    return render(request,'log_in/login.html')

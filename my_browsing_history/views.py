from django.shortcuts import render, redirect
from my_browsing_history.models import *
# Create your views here.
def MyBrowsingHistory(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    elif request.method == 'POST':
        pass
    else:
        return render(request, 'my_browsing_history/IBrowsed.html')

def MyBrowsingHistoryInner(request):
    return render(request, 'my_browsing_history/inner_IBrowsed.html')



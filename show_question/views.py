from django.shortcuts import render, redirect
#暂不导入models

# Create your views here.
def ShowQuestion(request):
    if not request.session.has_key('userName'):
        return redirect('login')
    elif request.method == 'POST':
        pass
    else:
        return render(request, 'show_question/article_single.html')

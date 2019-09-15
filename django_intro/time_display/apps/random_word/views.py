from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'counter' in request.session:
        request.session['counter']=int(request.session['counter'])+1
    else:
        request.session['counter']=1
    request.session['word']=get_random_string(length=14)
    return render(request, "random_word/index.html")

def reset(request):
    request.session['counter'] = 0
    return redirect("/random_word")

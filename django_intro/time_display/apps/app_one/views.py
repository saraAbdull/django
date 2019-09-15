from django.shortcuts import render, HttpResponse
from time import gmtime, strftime,localtime


def index(request):
    context = {
        "date": strftime("%Y-%m-%d" , localtime()),
        "time": strftime("%H:%M %p", localtime())
    }
    return render(request, "app_one/index.html", context)
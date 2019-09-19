from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        Book.objects.create(title = title ,desc =desc)
    context = {
    	"all": Book.objects.all().order_by("id")
    }
    return render(request,"books_authors_app/index.html", context)

def authors(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        nt = request.POST['note']
        author.objects.create(first_name =fname ,last_name =lname, notes=nt)
    context = {
    	"all": author.objects.all().order_by("id")
    }
    return render(request,"books_authors_app/authors.html",context)

def authDetails(request,id):
    context = {
    	"auth": author.objects.get(id=id)
    }
    return render(request,"books_authors_app/authDetails.html",context)

def bookDetails(request,id):
    context = {
    	"book": Book.objects.get(id=id)
    }
    return render(request,"books_authors_app/bookDetails.html",context)

# request.session['acts'].insert(0,"<p style='color:green;margin: 0px'>Earned "+str (r)+" golds from "+form+"!</p>")    
#     return redirect("/")

# def restart(request):
#     if request.method == "GET":
#         request.session.clear()
#     return redirect("/")

from django.shortcuts import render, redirect
import random

def home(request):
    if 'gold' not in request.session:
        request.session['gold']= 0
        request.session['acts']=[]
    #     session['attempts']=random.randint(1, 100)
    # print(session['random'])
    return render(request,"game/home.html")

def check(request):
    if request.method == "POST":
        form = request.POST['building']
        if form == 'farm':
            r=random.randint(10, 20)
            request.session['gold']+=r
        elif form == 'cave':
            r=random.randint(5, 10)
            request.session['gold']+=r
        elif form == 'house':
            r=random.randint(2, 5)
            request.session['gold']+=r
        else:
            r=random.randint(-50, 50)
            request.session['gold']+=r
        
        if r<0:
            request.session['acts'].insert(0,"<p style='color:red;margin: 0px'>Entered a "+form+" and lost "+str (r)+" golds... Ouch..!</p>")    
        else:
            request.session['acts'].insert(0,"<p style='color:green;margin: 0px'>Earned "+str (r)+" golds from "+form+"!</p>")    
    return redirect("/")

def restart(request):
    if request.method == "GET":
        request.session.clear()
    return redirect("/")
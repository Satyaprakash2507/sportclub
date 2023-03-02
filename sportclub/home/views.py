from home.models import Contact
from django.shortcuts import redirect, render,HttpResponse
from home.models import *

# Create your views here.
def homepage(request):
    return render(request,"homepage.html")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def register(request):
    return render(request,"register.html")
def contact(request):
    return render(request,"contact.html")
def services(request):
    return render(request,"services.html")
def payment(request):
    return render(request,"payment.html")
def score(request):
    return render(request,"score.html")
def contactaction(request):
    if request.method=='POST':
        fname=request.POST.get('firstname')   
        lname=request.POST.get('lastname') 
        email=request.POST.get('email1') 
        subject=request.POST.get('subject') 
        c=Contact(fname=fname, lname=lname, email=email, subject=subject)
        c.save()
        return render(request,"contact.html",{"msg":"massage successfully submitted"})

def registeraction(request):
    if request.method=='POST':
        tname=request.POST.get('TeamName')
        email=request.POST.get('Email')
        pnumber=request.POST.get('Phonenumber')
        tmember=request.POST.get('Teammember')
        sports=request.POST.get('Sports')
        agroup=request.POST.get('Agegroup')
        team=request.POST.get('Team')
        Match=request.POST.get('Match')
        r=register(tname=tname, email=email, pnumber=pnumber, tmember=tmember, sports=sports, agroup=agroup, team=team,match=Match )
        r.save()
        return render(request,"register.html",{"msg":"massage successfully submitted"})



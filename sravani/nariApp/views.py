from django.shortcuts import render
from nariApp import forms

# Create your views here.
def studentRegisterView(request):
    form=forms.StudentsRegistry()
    if request.method=="POST":
        form=forms.StudentsRegistry(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'nariApp/register.html',{"form":form})
def kitkatty(request):
    name="narendra"
    return render(request,"nariApp/kitkat.html",{"name":name})
def cook(request):
    count=int(request.COOKIES.get("count",0))
    newcount=count+1
    response=render(request,"nariApp/cookeee.html",{'count':newcount})
    response.set_cookie("count",newcount)
    return response
def horlicks(request):
    num=request.COOKIES.get("count")
    return render(request,"nariApp/demo.html",{"num":num})
def session(request):
    count1=request.session.get("count1",0)
    newcount=count1+1
    v="virataParvam"
    request.session["count1"]=newcount
    request.session["count2"]=v
    return render(request,"nariApp/cookeee.html",{"count1":newcount,"count2":v})

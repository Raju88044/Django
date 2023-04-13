from django.shortcuts import render,HttpResponse

def show(request):
    return render(request,'home.html',{'name':'Raju'})

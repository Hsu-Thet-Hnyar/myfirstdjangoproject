from django.shortcuts import render

# Create your views here.

def first(request):
    return render (request,'first.html',{})

def second(request):
    return render (request,'home.html',{})

def third(request):
    return render (request,'toysforgirls.html',{})

def fourth(request):
    return render (request,'toysforboys.html',{})

def fifth(request):
    return render (request,'contact.html',{})
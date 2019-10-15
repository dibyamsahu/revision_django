from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello")

def help(request):
    my_dict = {"insert_me":"This is the help page"}
    return render(request, "second_app/help.html", context=my_dict)

def leaves(request):
    return render(request, "second_app/leaves.html")

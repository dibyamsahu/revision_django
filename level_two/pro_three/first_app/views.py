from django.shortcuts import render
from first_app.models import UserDetail

# Create your views here.

def index(request):
    return render(request, "first_app/index.html")

def user_detail(request):
    user = UserDetail.objects.order_by("age")
    user_dict = {"detail":user}
    return render(request, "first_app/user.html",context=user_dict)
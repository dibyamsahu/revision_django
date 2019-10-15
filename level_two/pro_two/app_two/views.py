from django.shortcuts import render
from app_two.models import UserDetail
# Create your views here.
def index(request):
    return render(request, "index.html")

def user(request):
    user_list = UserDetail.objects.order_by("first_name")
    user_dict={"user":user_list}
    return render(request, "user.html", context=user_dict)
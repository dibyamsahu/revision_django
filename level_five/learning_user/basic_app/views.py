from django.shortcuts import render
from basic_app.models import UserProfileInfo
from basic_app.forms import UserProfileForm,UserProfileInfoForm
from django.contrib.auth.models import User

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def registrations(request):

    registered = False

    if request.method=="POST":
        user_form = UserProfileForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user #this is the one to one relationship with the user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

                profile.save()

                registered =True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserProfileForm()
        profile_form=UserProfileInfoForm()


    return render(request,'basic_app/registrations.html',
                  {"registered": registered,"user_form": user_form,"profile_form": profile_form})

def user_login(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse("index"))

            else:
                HttpResponse("User is not active")

        else:
            print("someone tried to login but failed")
            print("username {} and password{}".format(username,password))
            return HttpResponse("Invalid Credentials")

    else:
        return render(request,'basic_app/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
        


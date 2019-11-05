from django.shortcuts import render
from userapp import forms
# Create your views here.
def index(request):
    return render(request, 'userapp/index.html')

def user_form(request):
    form = forms.UserForm()

    if request.method=="POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'userapp/form_page.html', {'form':form})
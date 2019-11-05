from django import forms
from userapp.models import UserDetail

class UserForm(forms.ModelForm):
    
    class Meta:
        model = UserDetail
        fields = ("__all__")

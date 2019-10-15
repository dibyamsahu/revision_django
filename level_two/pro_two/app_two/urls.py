from django.conf.urls import url
from app_two import views

urlpatterns = [
    url(r"^$", views.user, name="user")
]

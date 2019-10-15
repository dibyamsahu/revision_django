from django.shortcuts import render
from app_one.models import Topic, AccessRecord, Webpage

# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {"acc_rec":webpage_list}
    return render(request, "app_one/index.html", context=date_dict)

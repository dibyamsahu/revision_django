from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from basic_app.models import School
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"

class SchoolListView(ListView):
    context_object_name = "schools"
    model = School

class SchoolDetailView(DetailView):
    context_object_name = "school_detail"    
    model = School
    template_name = "basic_app/school_detail.html"


class SchoolCreateView(CreateView):
    model = School
    fields = ("name", "principal", "address")
    
class SchoolUpdateView(UpdateView):
    model = School
    fields = ("name","principal")

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("basic_app:list")




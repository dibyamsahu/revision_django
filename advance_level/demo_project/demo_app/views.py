from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from demo_app.models import School
from django.urls import reverse_lazy
# Create your views here.


class IndexView(TemplateView):
    template_name = "index.html"


class SchoolListView(ListView):
    context_object_name = "schools"
    model = School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = School
    template_name = "demo_app/school_detail.html"

class SchoolCreateView(CreateView):
    model = School
    fields = ("name","principal","address")

class SchoolUpdateView(UpdateView):
    model=School
    fields = ("name","principal")

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("demo_app:list")


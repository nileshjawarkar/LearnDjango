from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from django.urls import reverse_lazy
from . import models

"""
def index( request ) :
    return render( request, "app01/index.html")


class IndexView( View ) :

    def get( self, request ) :
        return HttpResponse("This is the first view")

"""

class IndexView( TemplateView ):

    template_name = "app01/index.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["content"] = "This is home page"
        return data


class SchoolListView( ListView ) :
    model = models.School

class SchoolDetailView( DetailView ) :
    model = models.School
    # context_object_name = 'school_details'    
    # template_name = 'app01/school_detail.html'    

class SchoolCreateView( CreateView ) :
    fields = ("name",)
    model = models.School
    

class SchoolUpdateView( UpdateView ) :
    fields = ("name",)
    model = models.School
    

class SchoolDeleteView( DeleteView ) :
    model = models.School
    success_url = reverse_lazy("app01:list")
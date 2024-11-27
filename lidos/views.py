from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    """
    Displays the home page
    """
    template_name = 'index.html'
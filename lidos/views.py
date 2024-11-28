from django.shortcuts import render
from django.views import generic
from .models import Lido

# Create your views here.
class LidoList(generic.ListView):
    queryset = Lido.objects.filter(status=1)
    template_name = "lidos/index.html"
    paginate_by = 6
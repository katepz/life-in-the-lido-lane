from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Lido

# Create your views here.
class LidoList(generic.ListView):
    queryset = Lido.objects.filter(status=1)
    template_name = "lidos/index.html"
    paginate_by = 6

def lido_detail(request, slug):
    """
    Display an individual :model: `lidos.Lido`

    **Context**
    ``lido``
        An instance of :model: `lidos.Lido`
    
    **Template**
    :template:`lidos/lido_detail.html`
    """
    queryset = Lido.objects.filter(status=1)
    lido = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "lidos/lido_detail.html",
        {"lido": lido, "info": "Information:"}
    )
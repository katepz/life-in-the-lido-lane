from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Lido
from .forms import CommentForm


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
    comments = lido.comments.all().order_by("-created_on")
    comment_count = lido.comments.filter(is_approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user_id = request.user
            comment.lido = lido
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "lidos/lido_detail.html",
        {
            "lido": lido, 
            "info": "Information:", 
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )
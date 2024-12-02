from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Lido, Comment
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

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Lido.objects.filter(status=1)
        lido = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.user_id == request.user:
            comment = comment_form.save(commit=False)
            comment.lido = lido
            comment.is_approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('lido_detail', args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Lido.objects.filter(status=1)
    lido = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.user_id == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('lido_detail', args=[slug]))
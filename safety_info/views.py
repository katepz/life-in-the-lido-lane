from django.shortcuts import render
from django.contrib import messages
from .models import SafetyInfo, SafetySuggestion
from .forms import SafetySuggestionForm

# Create your views here.
def safety_info(request):

    """
    Renders the safety page
    """
    safetyinfo = SafetyInfo.objects.all().order_by('-created_on').first()
    safetysuggestion = SafetySuggestion.objects.all().order_by("tip")

    if request.method == "POST":
        safetysuggestion_form = SafetySuggestionForm(data=request.POST)
        if safetysuggestion_form.is_valid():
            safetytip = safetysuggestion_form.save(commit=False)
            safetytip.user_id = request.user
            safetytip.save()
            messages.add_message(
                request, messages.SUCCESS, 'Safety tip suggested and awaiting fact-checking'
            )
    safetysuggestion_form = SafetySuggestionForm()

    return render(
        request,
        "safety_info/safety.html",
        {
            "safetyinfo": safetyinfo, 
            "safetysuggestion": safetysuggestion,
            "safetysuggestion_form": safetysuggestion_form,
        },
    )

# def lido_detail(request, slug):

#     lido = get_object_or_404(queryset, slug=slug)
#     comments = lido.comments.all().order_by("-created_on")
#     comment_count = lido.comments.filter(is_approved=True).count()

#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
            # comment = comment_form.save(commit=False)
            # comment.user_id = request.user
            # comment.lido = lido
            # comment.save()
            # messages.add_message(
            #     request, messages.SUCCESS,'Comment submitted and awaiting approval'
            # )

    # comment_form = CommentForm()

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
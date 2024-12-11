from django.shortcuts import render
from django.contrib import messages
from .models import SafetyInfo, SafetySuggestion
from .forms import SafetySuggestionForm

# Create your views here.
def safety_info(request):

    """
    View to render the safety page
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
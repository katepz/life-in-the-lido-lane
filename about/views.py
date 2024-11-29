from django.shortcuts import render
from django.contrib import messages
from .models import About 
from .forms import SuggestionForm

# Create your views here.
def about_project(request):

    if request.method == "POST":
        suggestion_form = SuggestionForm(data=request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()
            messages.add_message(request, messages.SUCCESS, "Lido sugestion received! I endeavour to respond within 2 working days.")
    """ 
    Renders the About page
    """
    about = About.objects.all().order_by('-updated_on').first()
    suggestion_form = SuggestionForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about, 
            "suggestion_form": suggestion_form,
        },
    )
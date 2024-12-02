from django.shortcuts import render
from .models import SafetyInfo 

# Create your views here.
def safety_info(request):

    """
    Renders the safety page
    """
    safetyinfo = SafetyInfo.objects.all().order_by('-created_on').first()
    
    return render(
        request,
        "safety_info/safety.html",
        {
            "safetyinfo": safetyinfo, 
        },
    )
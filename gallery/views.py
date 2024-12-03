from django.shortcuts import render
from .models import GalleryPage


def gallery_page(request):
    """
    Renders the gallery page
    """
    gallery = GalleryPage.objects.all().order_by('-created_on').first()

    return render(
        request,
        "gallery/gallery.html",
        {"gallery": gallery},
    )
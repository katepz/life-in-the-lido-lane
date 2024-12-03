from django.shortcuts import render
from django.contrib import messages
from .models import GalleryPage, Photo
from .forms import PhotoForm



def gallery_page(request):
    """
    Renders the gallery page
    """
    gallery = GalleryPage.objects.all().order_by('-created_on').first()
    photos = Photo.objects.all().order_by('-uploaded_at')

    if request.method == "POST":
        photo_form = PhotoForm(data=request.POST)
        if  photo_form.is_valid():
            photo = photo_form.save(commit=False)
            photo.user_id = request.user
            photo.save()
            messages.add_message(
                request, messages.SUCCESS, 'Photo received, awaiting approval'
            )
    photo_form = PhotoForm()

    return render(
        request,
        "gallery/gallery.html",
        {"gallery": gallery, 
        "photos": photos,
        "photo_form": photo_form,
        },
    )
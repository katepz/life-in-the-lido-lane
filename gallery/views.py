from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import GalleryPage, Photo
from .forms import PhotoForm


def gallery_page(request):
    """
    Renders the gallery page
    """
    gallery = GalleryPage.objects.all().order_by('-created_on').first()
    photos = Photo.objects.all().order_by('-uploaded_at')

    if request.method == "POST":
        photo_form = PhotoForm(request.POST, request.FILES)
        if photo_form.is_valid():
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


@login_required
def update_photo(request, pk):
    """
    View to handle updating a photo's caption
    """
    photo = get_object_or_404(Photo, pk=pk, user_id=request.user)
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo updated successfully.")
            return redirect("gallery")
    else:
        form = PhotoForm(instance=photo)
    return render(request, "gallery/update_photo.html", {"form": form, "photo": photo})

@login_required
def delete_photo(request, pk):
    """
    View to handle photo deletion
    """
    photo = get_object_or_404(Photo, pk=pk, user_id=request.user)
    if request.method == "POST":
        photo.delete()
        messages.success(request, "Photo deleted successfully.")
        return redirect("gallery")
    return render(request, "gallery/delete_photo.html", {"photo": photo})

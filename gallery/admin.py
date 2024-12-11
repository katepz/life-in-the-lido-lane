from django.contrib import admin
from .models import Photo, GalleryPage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Photo)
class PhotoAdmin(SummernoteModelAdmin):

    summernote_fields = ('caption',)
    list_display = ('user_id', 'caption', 'is_approved')

@admin.register(GalleryPage)
class GalleryPageAdmin(SummernoteModelAdmin):

    summernote_fields = ('title', 'description',)
    list_display = ('title', 'created_on')

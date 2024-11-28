from django.contrib import admin
from .models import Lido, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Lido)
class LidoAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Comment)
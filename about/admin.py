from django.contrib import admin
from .models import About, Suggestion
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):

    list_display = ('lido_idea', 'read',)
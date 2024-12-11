from django.contrib import admin
from .models import SafetyInfo, SafetySuggestion
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(SafetyInfo)
class SafetyInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

@admin.register(SafetySuggestion)
class SafetySuggestionAdmin(SummernoteModelAdmin):
    summernote_fields = ('tip',)
    list_display = ('user_id', 'is_approved')
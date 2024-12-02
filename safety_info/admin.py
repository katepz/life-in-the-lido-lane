from django.contrib import admin
from .models import SafetyInfo
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(SafetyInfo)
class SafetyInfoAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
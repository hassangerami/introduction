from django.contrib import admin
from .models import Introduction


@admin.register(Introduction)
class IntroAdmin(admin.ModelAdmin):
    list_display = ['name']

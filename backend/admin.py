from django.contrib import admin
from .models import card, uses


@admin.register(card)
class cardAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "modified"]


@admin.register(uses)
class usesAdmin(admin.ModelAdmin):
    readonly_fields = ["timestamp"]

from django.contrib import admin
from .models import *

@admin.register(ReviewPost)
class ReviewPostAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['writer']
    list_display = ['title', 'writer', 'content', 'category', 'like']
    list_filter = ('writer',)
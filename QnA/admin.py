from django.contrib import admin
from .models import *


@admin.register(QuestionPost)
class QuestionPostAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['writer']
    list_display = ['title', 'writer', 'content', 'category', 'like', 'picked_answer']
    list_filter = ('writer',)


@admin.register(AnswerPost)
class AnswerPostAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['writer']
    list_display = ['question', 'writer', 'content', 'picked', 'like', ]
    list_filter = ('writer',)


@admin.register(QuestionPhoto)
class QuestionPhotoAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    list_display = ['question', 'photo', ]


@admin.register(QuestionComment)
class QuestionCommentAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['writer']
    list_display = ['question', 'writer', 'content', ]
    list_filter = ('writer',)


@admin.register(AnswerComment)
class AnswerCommentAdmin(admin.ModelAdmin):
    ordering = ['created_at']
    search_fields = ['writer']
    list_display = ['answer', 'writer', 'content', ]
    list_filter = ('writer',)



from django.contrib import admin
from .models import Board, File, Question, Answer


# Register your models here.

@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    list_display_links = ['id', 'title']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']


@admin.register(Question)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'is_answer']
    list_display_links = ['id', 'title']


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'content']
    list_display_links = ['id']

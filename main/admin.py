from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from main.models import Todo


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    fields = ('author', 'content')
    list_display = ('id', 'author', 'content')
    list_display_links = ('id',)
    search_fields = ('content', 'author')

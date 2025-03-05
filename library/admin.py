from django.contrib import admin
from .models import Books

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_date', 'added_on')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre', 'published_date')
    ordering = ('-added_on',)

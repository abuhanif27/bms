from django.contrib import admin
from .models import Books

admin.site.site_header = "BMS Administration"
admin.site.site_title = "BMS Admin Portal"
admin.site.index_title = "Welcome to the BMS Dashboard"

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'published_date', 'added_on')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre', 'published_date')
    ordering = ('-added_on',)

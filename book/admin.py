from django.contrib import admin
from .models import Book

# Register your models here.


# admin.site.register(Book):


# admin.site.unregister(Book)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'alternative_titles_en',
                     'alternative_titles_ja', 'authors', 'genres')
    list_display = ['title', 'authors', 'genres']
    list_filter = ('title', 'authors', 'genres')

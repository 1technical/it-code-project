from django.contrib import admin
from django.utils.safestring import mark_safe

from discography.models import *

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'get_html_photo',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Фото Артиста"

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year', 'get_html_photo', 'slug',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('artist', 'title',)}
    autocomplete_fields = ('artist',)
    ordering = ('artist', 'year',)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = "Обложка"

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('artist', 'album', 'track_number', 'title', 'duration',)
    list_display_links = ('album',)
    autocomplete_fields = ('album',)
    ordering = ('album', 'track_number',)
    list_per_page = 15

@admin.register(Review)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'album', 'created', 'active', 'rating',)
    list_filter = ('active', 'created', 'updated',)


from django.contrib import admin
from discography.models import *


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'year', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('artist',)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('album', 'track_number', 'title', 'duration',)
    list_display_links = ('album',)
    autocomplete_fields = ('album',)
    ordering = ['album']
    list_per_page = 15


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(Genre)

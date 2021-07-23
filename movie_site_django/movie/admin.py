from django.contrib import admin
from .models import Movie, Genre


class MovieAdmin(admin.ModelAdmin):
    list_display = ('moviecd', 'movienm', 'prdtyear', 'opendt', 'posterurl')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('genrealt', 'moviecd')


admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)

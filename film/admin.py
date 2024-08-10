from django.contrib import admin

from film.models import Film, Genre


# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'year',)
    filter_horizontal = ('genres',)




@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)



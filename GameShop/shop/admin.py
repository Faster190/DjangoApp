from django.contrib import admin

# Register your models here.
from .models import *

class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class GamesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Games, GamesAdmin)
admin.site.register(Genre, GenreAdmin)

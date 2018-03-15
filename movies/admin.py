from django.contrib import admin
from .models import movies, songs
# Register your models here.

admin.site.register(movies)
admin.site.register(songs)
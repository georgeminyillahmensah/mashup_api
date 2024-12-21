from django.contrib import admin

# Register your models here.
from .models import Character, Quote, Setting, Genre

admin.site.register(Character)
admin.site.register(Quote)
admin.site.register(Setting)
admin.site.register(Genre)

from django.contrib import admin

from api.models import Todo, Log

# Register your models here.

admin.site.register(Todo)
admin.site.register(Log)
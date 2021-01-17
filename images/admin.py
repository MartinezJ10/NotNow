from django.contrib import admin
from . import models


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id')


admin.site.register(models.Category)
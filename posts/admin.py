from django.contrib import admin
from . import models
admin.site.register(models.Post)
admin.site.register(models.Category)
admin.site.register(models.SearchWord)
admin.site.register(models.Comment)


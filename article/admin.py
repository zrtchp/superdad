from django.contrib import admin
from .models import ArticleColumn

class ArticleColumnAdmin(admin.ModelAdmin):
    list_display = ("column",)

admin.site.register(ArticleColumn, ArticleColumnAdmin)
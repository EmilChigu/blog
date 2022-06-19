from django.contrib import admin

# Register your models here.

from . models import Article, Comment

# REGISTER MODEL WITH ADMIN PANEL
admin.site.register(Article)
admin.site.register(Comment)
from django.contrib import admin
from .models import Article, People

# Register your models here.

# admin.site.register(Article)


@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ("title", "description")
    list_display = ("title", "description")


@admin.register(People)
class PeopleModel(admin.ModelAdmin):
    list_filter = ("timestamp",)
    list_display = ("fname", "lname", "person_id", "timestamp")

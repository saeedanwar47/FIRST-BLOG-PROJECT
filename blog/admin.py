from django.contrib import admin
from .models import Category, Post


# Register your models here.

# custom admin models

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Description', 'add_date')

    search_fields = ('Title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('Title',)

    search_fields = ('Title',)

    list_filter = ('cat',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

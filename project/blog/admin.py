from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'author', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    readonly_fields = ('created_at',)
    save_on_top = True
    fields = ('title', 'slug', 'author', 'content', 'category', 'created_at')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)



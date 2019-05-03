from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'available', 'created', 'updated'
    ]
    list_editable = [
        'available'
    ]
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)



from django.contrib import admin
from .models import *

# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nom',              {'fields': ['name']}),
        ('Description',      {'fields': ['content']}),
        ('Type',             {'fields': ['type']}),
        ('Date de cr"ation', {'fields': ['created_at']}),
    ]
    list_display = ('name', 'content', 'type')
    list_filter = ['type', 'name']
    search_fields = ['name', 'content']

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(News)
from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['content']}),
        ('Informations de publication', {'fields': ['created_at'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    
    list_display = ('name', 'created_at', 'was_published_recently')
    
    list_filter = ['created_at']
    
    search_fields = ['content']

admin.site.register(Question, QuestionAdmin)

from django.contrib import admin
from .models import Snippet

# Register your models here.
class SnippetAdmin(admin.ModelAdmin):
    list_display=('created','title')
admin.site.register(Snippet,SnippetAdmin)
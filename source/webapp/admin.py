from django.contrib import admin
from webapp.models import ToDoList

class ToDoListAdmin(admin.ModelAdmin):
    list_display = ['pk', 'description', 'status', 'done_at']
    list_filter = ['status']
    list_display_links = ['pk', 'description']
    search_fields = ['description', 'status']
    fields = ['description', 'status', 'done_at']
    readonly_fields = ['done_at']



admin.site.register(ToDoList, ToDoListAdmin)
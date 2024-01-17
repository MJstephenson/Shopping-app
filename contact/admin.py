from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
   class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'subject', 'email', 'timestamp')
    search_fields = ('first_name', 'surname', 'email', 'subject')
    actions = ['delete_selected']

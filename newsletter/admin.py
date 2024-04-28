from django.contrib import admin
from .models import Subscriber


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'id')
    search_fields = ('email',)
    list_filter = ('email',)


admin.site.register(Subscriber, SubscriberAdmin)

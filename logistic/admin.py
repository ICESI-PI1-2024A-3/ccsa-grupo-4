from django.contrib import admin
from .models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    readonly_fields = ("registerDate", )


admin.site.register(Event, EventAdmin)

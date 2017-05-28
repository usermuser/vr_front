from django.contrib import admin

from .models import Process

class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time','stop_time','duration')
    list_filter = ['stop_time']

admin.site.register(Process,ProcessAdmin)

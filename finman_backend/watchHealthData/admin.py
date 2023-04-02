from django.contrib import admin
from .models import WatchHealthData


# Register your models here.
class WatchDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'watch_id', 'time', 'value', 'type')


admin.site.register(WatchHealthData, WatchDataAdmin)

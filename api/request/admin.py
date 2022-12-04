from django.contrib import admin

from . import models

class RequestModelAdmin(admin.ModelAdmin):
    list_display = ("camp_event", "representative", "child")


admin.site.register(models.RequestModel, RequestModelAdmin)

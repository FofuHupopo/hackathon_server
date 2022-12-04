from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from . import models

class CampEventModelAdmin(admin.ModelAdmin):
    list_display = ("title", "camp_organization", "view_requests")

    @admin.display(description="Заявки")
    def view_requests(self, obj):
        url = (
            reverse("admin:request_requestmodel_changelist")
            + "?"
            + urlencode({"camp_event": f"{obj.id}"})
        )
        return format_html('<a href="{}">Просмотреть заявки</a>', url)

class CampOrganizationModelAdmin(admin.ModelAdmin):
    list_display = ("title",)


admin.site.register(models.CampEventModel, CampEventModelAdmin)
admin.site.register(models.CampOrganizationModel, CampOrganizationModelAdmin)

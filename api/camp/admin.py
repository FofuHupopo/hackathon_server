from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from . import models

class CampEventModelAdmin(admin.ModelAdmin):
    list_display = ("title", "camp_organization", "view_requests", "export_requests")

    @admin.display(description="Заявки")
    def view_requests(self, obj):
        url = (
            reverse("admin:request_requestmodel_changelist")
            + "?"
            + urlencode({"camp_event": f"{obj.id}"})
        )
        return format_html('<a href="{}">Просмотреть заявки</a>', url)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(camp_organization__user=request.user)

    @admin.display(description="Экспорт заявок")
    def export_requests(self, obj):
        url = (
            reverse("admin:request_requestmodel_changelist")
            + f"?camp_event_id={obj.id}"
        )
        return format_html('<a href="{}">Скачать в .xlsx</a>', url)

class CampOrganizationModelAdmin(admin.ModelAdmin):
    list_display = ("title",)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(user=request.user)


admin.site.register(models.CampEventModel, CampEventModelAdmin)
admin.site.register(models.CampOrganizationModel, CampOrganizationModelAdmin)

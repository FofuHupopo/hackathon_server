from django.contrib import admin

from . import models

class RequestModelAdmin(admin.ModelAdmin):
    list_display = ("camp_event", "representative", "child")
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(
            camp_event__camp_organization__user=request.user
        )


admin.site.register(models.RequestModel, RequestModelAdmin)

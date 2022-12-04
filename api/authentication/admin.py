from django.contrib.auth.models import Group
from django.contrib import admin

from . import models


class UserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname")


admin.site.register(models.UserModel, UserModelAdmin)
# admin.site.register(models.ConfirmCodeModel)

admin.site.unregister(Group)

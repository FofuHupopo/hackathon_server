from django.contrib.auth.models import Group
from django.contrib import admin

from . import models


admin.site.register(models.UserModel)
# admin.site.register(models.ConfirmCodeModel)

admin.site.unregister(Group)

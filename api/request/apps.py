from django.apps import AppConfig


class RequestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.request'
    verbose_name = "Заявки"

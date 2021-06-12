from django.apps import AppConfig


class InjectionappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'InjectionApp'
    verbose_name = 'Инъекция sql'
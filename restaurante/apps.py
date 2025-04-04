from django.apps import AppConfig
from django.db.models.signals import post_migrate


class RestauranteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurante'
    def ready(self):
        post_migrate.connect(create_default_values, sender=self)


def create_default_values(sender, **kwargs):
    from .models import Categoria
    Categoria.create_default_values()
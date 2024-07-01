# Тут инфа о том, что за приложение и какой тип данных для создания таблицы

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "products"

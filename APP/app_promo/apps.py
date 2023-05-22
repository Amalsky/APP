from django.apps import AppConfig

from django.contrib.admin.apps import AdminConfig


class AppAdminConfig(AdminConfig):
    default_site = "app_promo.admin.AppAdmin"


class AppPromoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app_promo"

    def ready(self):
        import app_promo.signal

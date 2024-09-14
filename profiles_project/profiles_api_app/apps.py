from django.apps import AppConfig


class ProfilesApiAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "profiles_api_app"


    def ready(self):
        import profiles_api_app.signals

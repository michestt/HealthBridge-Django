from django.apps import AppConfig


class HealthprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'healthprofile'


class healthprofileAppConfig(AppConfig):
    name = 'healthprofile'

    def ready(self):
        import healthprofile.signals

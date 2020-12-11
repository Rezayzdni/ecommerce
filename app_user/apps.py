from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'app_user'

    def ready(self):
        import app_user.signals

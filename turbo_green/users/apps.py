from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "turbo_green.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import turbo_green.users.signals  # noqa F401
        except ImportError:
            pass

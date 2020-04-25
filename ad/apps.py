from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class AdConfig(AppConfig):
    name = 'ad'


def ready(self):
        import ad.signals  # noqa

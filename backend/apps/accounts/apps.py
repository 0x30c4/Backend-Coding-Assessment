from django.apps import AppConfig
from django.conf import settings
import os

class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    # path = os.path.join(settings.BASE_DIR, 'apps.accounts')

    class Meta:
        app_label = 'apps.accounts'

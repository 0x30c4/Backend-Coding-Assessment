from django.apps import AppConfig
from django.conf import settings
import os

class GalleryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.gallery'
    # path = os.path.join(settings.BASE_DIR, 'apps.gallery')

    class Meta:
        app_label = 'apps.gallery'

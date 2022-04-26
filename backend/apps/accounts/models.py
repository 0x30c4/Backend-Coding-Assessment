from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    """
    Custom User model that can handle email.
    """
    email = models.EmailField(_('email address'), unique=True)

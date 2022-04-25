from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        # Check if the username is a valid email address or not.
        # If not then raise an invalid email error.

        try:
            validate_email(username)
        except ValidationError as e:
            raise e

        try:
            user = UserModel.objects.get(Q(email__iexact=username))

        except UserModel.DoesNotExist:

            # Create a new user if the user doesn't exists.
            # make username from email.
            _username = username.split("@")[0]
            new_user = UserModel.objects.create_user(
                username=_username,
                email=username,
                password=password
            )
            return new_user
        except Exception as e:
            raise e

        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(email__iexact=username)).order_by('id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user

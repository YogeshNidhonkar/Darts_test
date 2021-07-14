""" User manager """

from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):

    """Custom manager for Email."""

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        is_active = extra_fields.pop("is_active", True)
        user = self.model(email=email, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          joining_date=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.

        """
        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(email, password, is_staff, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.
        """
        extra_fields.pop("is_staff", False)
        return self._create_user(email, password, True, True, **extra_fields)

    def create(self, email, password=None, **extra_fields):
        """
        Create and save an EmailUser with the given email and password.

        """

        is_staff = extra_fields.pop("is_staff", False)
        return self._create_user(email, password, is_staff, False, **extra_fields)

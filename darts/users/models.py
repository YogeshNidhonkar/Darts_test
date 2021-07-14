""" User model to store logged in user information  """

from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, )
from django.utils import timezone
from django.core.validators import (MaxValueValidator, MinValueValidator)
from django.utils.translation import ugettext_lazy as _
from users.manager import UserManager
# Create your models here.

MALE = 'male'
FEMALE = 'female'
OTHER = 'other'
GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other')
)


class User(AbstractBaseUser, PermissionsMixin):
    """ Model for storing each user information(student and staff both)
        if is_staff is True then user is a Staff member else user is a student"""
    full_name = models.CharField(_('Full Name'), max_length=255)
    email = models.EmailField(_('Email Address'), max_length=255, unique=True)
    gender = models.CharField(_('Gender'), choices=GENDER, max_length=255,
                              default=GENDER[0][0], null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=False)
    joining_date = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name', 'is_staff')

    objects = UserManager()

    def __str__(self):
        return "{}".format(self.full_name)

class Student(models.Model):
    """ Model for storing each student information """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student')
    standard = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return "{} {}".format(self.user, self.standard)

""" Marks Model """

from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)
from django.utils.translation import ugettext_lazy as _

from users.models import Student
# Create your models here.

MATHS = 'maths'
SCIENCE = 'science'
HISTORY = 'history'
GEOGRAPHY = 'geography'
ENGLISH = 'english'

SUBJECT = (
    (MATHS, 'MATHS'),
    (SCIENCE, 'science'),
    (HISTORY, 'history'),
    (GEOGRAPHY, 'geography'),
    (ENGLISH, 'english')
)

class Marks(models.Model):
    """ Model for storing each student information """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.CharField(_('Subject'), choices=SUBJECT, max_length=255)
    marks = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return "{} {}".format(self.subject, self.marks)

    class Meta:
        unique_together = ('student', 'subject',)

""" Admin panel for marks """

from django.contrib import admin
from . import models


class MarksAdmin(admin.ModelAdmin):
    """
    Buyer Admin
    """
    model = models.Marks

admin.site.register(models.Marks, MarksAdmin)

"""
User Admin models
"""
from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    """
    User Admin
    """
    model = models.User
    list_display = ('full_name', 'email', 'gender')
    # readonly_fields = ('id', 'created_at')
    # ordering = ('-created_at', )
    search_fields = ('email',)
    list_filter = ('is_staff',)

admin.site.register(models.User, UserAdmin)

class StudentAdmin(admin.ModelAdmin):
    """
    Student Admin
    """
    model = models.Student
admin.site.register(models.Student, StudentAdmin)

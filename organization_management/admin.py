from django.contrib import admin
from django import forms

from . import models


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = "__all__"


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = [
        "reporting_manager_name",
        "reporting_manager_email",
        "first_time_login",
        "signature",
        "created",
        "reporting_manager_uuid",
        "id",
        "last_updated",
    ]
    readonly_fields = [
        "reporting_manager_name",
        "reporting_manager_email",
        "first_time_login",
        "signature",
        "created",
        "reporting_manager_uuid",
        "id",
        "last_updated",
    ]


admin.site.register(models.User, UserAdmin)

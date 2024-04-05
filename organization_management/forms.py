from django import forms
from . import models


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "reporting_manager_name",
            "reporting_manager_email",
            "first_time_login",
            "signature",
            "reporting_manager_uuid",
        ]

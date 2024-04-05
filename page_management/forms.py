from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from . import models


class PagesForm(forms.ModelForm):
    class Meta:
        model = models.Pages
        fields = [
            "publish_down",
            "slug",
            "page_title",
            "publish",
            "is_active",
            "is_home_page",
            "page_content",
            "content_type",
            "users",
            "groups",
        ]

    def __init__(self, *args, **kwargs):
        super(PagesForm, self).__init__(*args, **kwargs)
        self.fields["users"].queryset = User.objects.all()
        self.fields["groups"].queryset = Group.objects.all()


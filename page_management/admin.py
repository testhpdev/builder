from django.contrib import admin
from django import forms

from . import models


class PagesAdminForm(forms.ModelForm):

    class Meta:
        model = models.Pages
        fields = "__all__"


class PagesAdmin(admin.ModelAdmin):
    form = PagesAdminForm
    list_display = [
        "publish_down",
        "slug",
        "page_title",
        "publish",
        "is_active",
        "is_home_page",
        "page_content",
        "last_updated",
        "content_type",
        "created",
        "id",
    ]
    readonly_fields = [
        "publish_down",
        "slug",
        "page_title",
        "publish",
        "is_active",
        "is_home_page",
        "page_content",
        "last_updated",
        "content_type",
        "created",
        "id",
    ]


admin.site.register(models.Pages, PagesAdmin)

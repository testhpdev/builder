from rest_framework import serializers

from . import models


class PagesSerializer(serializers.ModelSerializer):

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
            "last_updated",
            "content_type",
            "created",
            "id",
            "users",
            "groups",
        ]

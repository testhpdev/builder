from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "reporting_manager_name",
            "reporting_manager_email",
            "first_time_login",
            "signature",
            "created",
            "reporting_manager_uuid",
            "id",
            "last_updated",
        ]

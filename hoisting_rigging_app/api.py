from rest_framework import viewsets, permissions

from . import serializers
from . import models


class appFormViewSet(viewsets.ModelViewSet):
    """ViewSet for the appForm class"""

    queryset = models.appForm.objects.all()
    serializer_class = serializers.appFormSerializer
    permission_classes = [permissions.IsAuthenticated]


class liftDescriptionViewSet(viewsets.ModelViewSet):
    """ViewSet for the liftDescription class"""

    queryset = models.liftDescription.objects.all()
    serializer_class = serializers.liftDescriptionSerializer
    permission_classes = [permissions.IsAuthenticated]


class mobileCraneViewSet(viewsets.ModelViewSet):
    """ViewSet for the mobileCrane class"""

    queryset = models.mobileCrane.objects.all()
    serializer_class = serializers.mobileCraneSerializer
    permission_classes = [permissions.IsAuthenticated]


class overheadCraneViewSet(viewsets.ModelViewSet):
    """ViewSet for the overheadCrane class"""

    queryset = models.overheadCrane.objects.all()
    serializer_class = serializers.overheadCraneSerializer
    permission_classes = [permissions.IsAuthenticated]


class tools_hardwareViewSet(viewsets.ModelViewSet):
    """ViewSet for the tools_hardware class"""

    queryset = models.tools_hardware.objects.all()
    serializer_class = serializers.tools_hardwareSerializer
    permission_classes = [permissions.IsAuthenticated]

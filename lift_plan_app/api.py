from rest_framework import viewsets, permissions

from . import serializers
from . import models


class equipmentsListViewSet(viewsets.ModelViewSet):
    """ViewSet for the equipmentsList class"""

    queryset = models.equipmentsList.objects.all()
    serializer_class = serializers.equipmentsListSerializer
    permission_classes = [permissions.IsAuthenticated]


class liftDescriptionsViewSet(viewsets.ModelViewSet):
    """ViewSet for the liftDescriptions class"""

    queryset = models.liftDescriptions.objects.all()
    serializer_class = serializers.liftDescriptionsSerializer
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


class planAttachmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the planAttachment class"""

    queryset = models.planAttachment.objects.all()
    serializer_class = serializers.planAttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class planFormViewSet(viewsets.ModelViewSet):
    """ViewSet for the planForm class"""

    queryset = models.planForm.objects.all()
    serializer_class = serializers.planFormSerializer
    permission_classes = [permissions.IsAuthenticated]


class planSketchViewSet(viewsets.ModelViewSet):
    """ViewSet for the planSketch class"""

    queryset = models.planSketch.objects.all()
    serializer_class = serializers.planSketchSerializer
    permission_classes = [permissions.IsAuthenticated]


class workAssignmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the workAssignment class"""

    queryset = models.workAssignment.objects.all()
    serializer_class = serializers.workAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

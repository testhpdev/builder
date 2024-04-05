from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PagesViewSet(viewsets.ModelViewSet):
    """ViewSet for the Pages class"""

    queryset = models.Pages.objects.all()
    serializer_class = serializers.PagesSerializer
    permission_classes = [permissions.IsAuthenticated]

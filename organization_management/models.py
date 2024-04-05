from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    # Fields
    reporting_manager_name = models.CharField(max_length=200)
    reporting_manager_email = models.EmailField()
    first_time_login = models.BooleanField()
    signature = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    reporting_manager_uuid = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("organization_management_User_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("organization_management_User_update", args=(self.pk,))


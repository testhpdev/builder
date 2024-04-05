from django.db import models
from django.urls import reverse


class Pages(models.Model):

    # Relationships
    users = models.ManyToManyField("auth.User")
    groups = models.ManyToManyField("auth.Group")

    # Fields
    publish_down = models.DateTimeField()
    slug = models.SlugField()
    page_title = models.TextField(max_length=100)
    publish = models.DateTimeField()
    is_active = models.BooleanField()
    is_home_page = models.BooleanField()
    page_content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    content_type = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("page_management_Pages_detail", args=(self.slug,))

    def get_update_url(self):
        return reverse("page_management_Pages_update", args=(self.slug,))


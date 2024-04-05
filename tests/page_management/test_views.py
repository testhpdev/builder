import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Pages_list_view(client):
    instance1 = test_helpers.create_page_management_Pages()
    instance2 = test_helpers.create_page_management_Pages()
    url = reverse("page_management_Pages_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Pages_create_view(client):
    users = test_helpers.create_User()
    groups = test_helpers.create_Group()
    url = reverse("page_management_Pages_create")
    data = {
        "publish_down": datetime.now(),
        "slug": "slug",
        "page_title": "text",
        "publish": datetime.now(),
        "is_active": True,
        "is_home_page": True,
        "page_content": "text",
        "content_type": "text",
        "users": users.pk,
        "groups": groups.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Pages_detail_view(client):
    instance = test_helpers.create_page_management_Pages()
    url = reverse("page_management_Pages_detail", args=[instance.slug, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Pages_update_view(client):
    users = test_helpers.create_User()
    groups = test_helpers.create_Group()
    instance = test_helpers.create_page_management_Pages()
    url = reverse("page_management_Pages_update", args=[instance.slug, ])
    data = {
        "publish_down": datetime.now(),
        "slug": "slug",
        "page_title": "text",
        "publish": datetime.now(),
        "is_active": True,
        "is_home_page": True,
        "page_content": "text",
        "content_type": "text",
        "users": users.pk,
        "groups": groups.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

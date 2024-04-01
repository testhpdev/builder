import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_appForm_list_view(client):
    instance1 = test_helpers.create_hoisting_rigging_app_appForm()
    instance2 = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_appForm_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_appForm_create_view(client):
    reviewed_by = test_helpers.create_User()
    approved_by = test_helpers.create_User()
    crane_operator = test_helpers.create_User()
    rigger = test_helpers.create_User()
    flm = test_helpers.create_User()
    signaler = test_helpers.create_User()
    supervisor_of_lift = test_helpers.create_User()
    prepared_by = test_helpers.create_User()
    other = test_helpers.create_User()
    url = reverse("hoisting_rigging_app_appForm_create")
    data = {
        "special_instructions": "text",
        "form_type": "text",
        "form_status": "text",
        "lift_plan_sketch_description": "text",
        "lift_plan_sketch_image": "anImage",
        "reason": "text",
        "equipment": "text",
        "floor_plan_sketch_image": "anImage",
        "swp_jsa": "text",
        "floor_plan_sketch_description": "text",
        "usi_sci": "text",
        "hazardous_toxic_material": True,
        "reviewed_by": reviewed_by.pk,
        "approved_by": approved_by.pk,
        "crane_operator": crane_operator.pk,
        "rigger": rigger.pk,
        "flm": flm.pk,
        "signaler": signaler.pk,
        "supervisor_of_lift": supervisor_of_lift.pk,
        "prepared_by": prepared_by.pk,
        "other": other.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_appForm_detail_view(client):
    instance = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_appForm_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_appForm_update_view(client):
    reviewed_by = test_helpers.create_User()
    approved_by = test_helpers.create_User()
    crane_operator = test_helpers.create_User()
    rigger = test_helpers.create_User()
    flm = test_helpers.create_User()
    signaler = test_helpers.create_User()
    supervisor_of_lift = test_helpers.create_User()
    prepared_by = test_helpers.create_User()
    other = test_helpers.create_User()
    instance = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_appForm_update", args=[instance.pk, ])
    data = {
        "special_instructions": "text",
        "form_type": "text",
        "form_status": "text",
        "lift_plan_sketch_description": "text",
        "lift_plan_sketch_image": "anImage",
        "reason": "text",
        "equipment": "text",
        "floor_plan_sketch_image": "anImage",
        "swp_jsa": "text",
        "floor_plan_sketch_description": "text",
        "usi_sci": "text",
        "hazardous_toxic_material": True,
        "reviewed_by": reviewed_by.pk,
        "approved_by": approved_by.pk,
        "crane_operator": crane_operator.pk,
        "rigger": rigger.pk,
        "flm": flm.pk,
        "signaler": signaler.pk,
        "supervisor_of_lift": supervisor_of_lift.pk,
        "prepared_by": prepared_by.pk,
        "other": other.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_liftDescription_list_view(client):
    instance1 = test_helpers.create_hoisting_rigging_app_liftDescription()
    instance2 = test_helpers.create_hoisting_rigging_app_liftDescription()
    url = reverse("hoisting_rigging_app_liftDescription_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_liftDescription_create_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_liftDescription_create")
    data = {
        "estimate_calculated_measured": "text",
        "c_of_g_12_of_load_centre": True,
        "load_weight": "text",
        "load_items": "text",
        "total_weight": "text",
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_liftDescription_detail_view(client):
    instance = test_helpers.create_hoisting_rigging_app_liftDescription()
    url = reverse("hoisting_rigging_app_liftDescription_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_liftDescription_update_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    instance = test_helpers.create_hoisting_rigging_app_liftDescription()
    url = reverse("hoisting_rigging_app_liftDescription_update", args=[instance.pk, ])
    data = {
        "estimate_calculated_measured": "text",
        "c_of_g_12_of_load_centre": True,
        "load_weight": "text",
        "load_items": "text",
        "total_weight": "text",
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_mobileCrane_list_view(client):
    instance1 = test_helpers.create_hoisting_rigging_app_mobileCrane()
    instance2 = test_helpers.create_hoisting_rigging_app_mobileCrane()
    url = reverse("hoisting_rigging_app_mobileCrane_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_mobileCrane_create_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_mobileCrane_create")
    data = {
        "parts_of_line": "text",
        "capacity": "text",
        "equipment_number": "text",
        "block_ball_size": "text",
        "crane_type": "text",
        "boom_sections": "text",
        "manufacturer": "text",
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_mobileCrane_detail_view(client):
    instance = test_helpers.create_hoisting_rigging_app_mobileCrane()
    url = reverse("hoisting_rigging_app_mobileCrane_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_mobileCrane_update_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    instance = test_helpers.create_hoisting_rigging_app_mobileCrane()
    url = reverse("hoisting_rigging_app_mobileCrane_update", args=[instance.pk, ])
    data = {
        "parts_of_line": "text",
        "capacity": "text",
        "equipment_number": "text",
        "block_ball_size": "text",
        "crane_type": "text",
        "boom_sections": "text",
        "manufacturer": "text",
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_overheadCrane_list_view(client):
    instance1 = test_helpers.create_hoisting_rigging_app_overheadCrane()
    instance2 = test_helpers.create_hoisting_rigging_app_overheadCrane()
    url = reverse("hoisting_rigging_app_overheadCrane_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_overheadCrane_create_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_overheadCrane_create")
    data = {
        "equipment_name": "text",
        "equipment_code": "text",
        "auxiliary_hook_capacity": "text",
        "main_hook_capacity": "text",
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_overheadCrane_detail_view(client):
    instance = test_helpers.create_hoisting_rigging_app_overheadCrane()
    url = reverse("hoisting_rigging_app_overheadCrane_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_overheadCrane_update_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    instance = test_helpers.create_hoisting_rigging_app_overheadCrane()
    url = reverse("hoisting_rigging_app_overheadCrane_update", args=[instance.pk, ])
    data = {
        "equipment_name": "text",
        "equipment_code": "text",
        "auxiliary_hook_capacity": "text",
        "main_hook_capacity": "text",
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_tools_hardware_list_view(client):
    instance1 = test_helpers.create_hoisting_rigging_app_tools_hardware()
    instance2 = test_helpers.create_hoisting_rigging_app_tools_hardware()
    url = reverse("hoisting_rigging_app_tools_hardware_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_tools_hardware_create_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    url = reverse("hoisting_rigging_app_tools_hardware_create")
    data = {
        "capacity": "text",
        "weight": "text",
        "tool_number": "text",
        "description": "text",
        "tension": "text",
        "type": "text",
        "quantity": 1,
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_tools_hardware_detail_view(client):
    instance = test_helpers.create_hoisting_rigging_app_tools_hardware()
    url = reverse("hoisting_rigging_app_tools_hardware_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_tools_hardware_update_view(client):
    appFormId = test_helpers.create_hoisting_rigging_app_appForm()
    instance = test_helpers.create_hoisting_rigging_app_tools_hardware()
    url = reverse("hoisting_rigging_app_tools_hardware_update", args=[instance.pk, ])
    data = {
        "capacity": "text",
        "weight": "text",
        "tool_number": "text",
        "description": "text",
        "tension": "text",
        "type": "text",
        "quantity": 1,
        "appFormId": appFormId.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

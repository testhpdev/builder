import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_equipmentsList_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_equipmentsList()
    instance2 = test_helpers.create_lift_plan_app_equipmentsList()
    url = reverse("lift_plan_app_equipmentsList_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_equipmentsList_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_equipmentsList_create")
    data = {
        "type": "text",
        "capacity": "text",
        "tension": "text",
        "description": "text",
        "weight": "text",
        "tool_number": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_equipmentsList_detail_view(client):
    instance = test_helpers.create_lift_plan_app_equipmentsList()
    url = reverse("lift_plan_app_equipmentsList_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_equipmentsList_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    instance = test_helpers.create_lift_plan_app_equipmentsList()
    url = reverse("lift_plan_app_equipmentsList_update", args=[instance.pk, ])
    data = {
        "type": "text",
        "capacity": "text",
        "tension": "text",
        "description": "text",
        "weight": "text",
        "tool_number": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_liftDescriptions_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_liftDescriptions()
    instance2 = test_helpers.create_lift_plan_app_liftDescriptions()
    url = reverse("lift_plan_app_liftDescriptions_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_liftDescriptions_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_liftDescriptions_create")
    data = {
        "load_items": "text",
        "load_centre": True,
        "load_weight": "text",
        "total_weight": "text",
        "estimation": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_liftDescriptions_detail_view(client):
    instance = test_helpers.create_lift_plan_app_liftDescriptions()
    url = reverse("lift_plan_app_liftDescriptions_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_liftDescriptions_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    instance = test_helpers.create_lift_plan_app_liftDescriptions()
    url = reverse("lift_plan_app_liftDescriptions_update", args=[instance.pk, ])
    data = {
        "load_items": "text",
        "load_centre": True,
        "load_weight": "text",
        "total_weight": "text",
        "estimation": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_mobileCrane_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_mobileCrane()
    instance2 = test_helpers.create_lift_plan_app_mobileCrane()
    url = reverse("lift_plan_app_mobileCrane_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_mobileCrane_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_mobileCrane_create")
    data = {
        "crane_type": "text",
        "block_ball_size": "text",
        "boom_sections": "text",
        "manufacturer_restrictions": "text",
        "parts_of_line": "text",
        "capacity": "text",
        "manufacturer": "text",
        "equipment_number": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_mobileCrane_detail_view(client):
    instance = test_helpers.create_lift_plan_app_mobileCrane()
    url = reverse("lift_plan_app_mobileCrane_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_mobileCrane_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    instance = test_helpers.create_lift_plan_app_mobileCrane()
    url = reverse("lift_plan_app_mobileCrane_update", args=[instance.pk, ])
    data = {
        "crane_type": "text",
        "block_ball_size": "text",
        "boom_sections": "text",
        "manufacturer_restrictions": "text",
        "parts_of_line": "text",
        "capacity": "text",
        "manufacturer": "text",
        "equipment_number": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_overheadCrane_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_overheadCrane()
    instance2 = test_helpers.create_lift_plan_app_overheadCrane()
    url = reverse("lift_plan_app_overheadCrane_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_overheadCrane_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_overheadCrane_create")
    data = {
        "equipment_code": "text",
        "auxiliary_hook_capacity": "text",
        "equipment_name": "text",
        "main_hook_capacity": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_overheadCrane_detail_view(client):
    instance = test_helpers.create_lift_plan_app_overheadCrane()
    url = reverse("lift_plan_app_overheadCrane_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_overheadCrane_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    instance = test_helpers.create_lift_plan_app_overheadCrane()
    url = reverse("lift_plan_app_overheadCrane_update", args=[instance.pk, ])
    data = {
        "equipment_code": "text",
        "auxiliary_hook_capacity": "text",
        "equipment_name": "text",
        "main_hook_capacity": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_planAttachment_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_planAttachment()
    instance2 = test_helpers.create_lift_plan_app_planAttachment()
    url = reverse("lift_plan_app_planAttachment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_planAttachment_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_planAttachment_create")
    data = {
        "file_path": "aFile",
        "file_attachment": "aFile",
        "label": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_planAttachment_detail_view(client):
    instance = test_helpers.create_lift_plan_app_planAttachment()
    url = reverse("lift_plan_app_planAttachment_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_planAttachment_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    instance = test_helpers.create_lift_plan_app_planAttachment()
    url = reverse("lift_plan_app_planAttachment_update", args=[instance.pk, ])
    data = {
        "file_path": "aFile",
        "file_attachment": "aFile",
        "label": "text",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_planForm_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_planForm()
    instance2 = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_planForm_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_planForm_create_view(client):
    reviewed_by = test_helpers.create_User()
    prepared_by = test_helpers.create_User()
    approved_by = test_helpers.create_User()
    url = reverse("lift_plan_app_planForm_create")
    data = {
        "reason_for_lift": "text",
        "hazardous_or_toxic": True,
        "usi_sci": "text",
        "equipment": "text",
        "form_status": "text",
        "swp_jsa": "text",
        "special_instructions": "text",
        "reviewed_by": reviewed_by.pk,
        "prepared_by": prepared_by.pk,
        "approved_by": approved_by.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_planForm_detail_view(client):
    instance = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_planForm_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_planForm_update_view(client):
    reviewed_by = test_helpers.create_User()
    prepared_by = test_helpers.create_User()
    approved_by = test_helpers.create_User()
    instance = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_planForm_update", args=[instance.pk, ])
    data = {
        "reason_for_lift": "text",
        "hazardous_or_toxic": True,
        "usi_sci": "text",
        "equipment": "text",
        "form_status": "text",
        "swp_jsa": "text",
        "special_instructions": "text",
        "reviewed_by": reviewed_by.pk,
        "prepared_by": prepared_by.pk,
        "approved_by": approved_by.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_planSketch_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_planSketch()
    instance2 = test_helpers.create_lift_plan_app_planSketch()
    url = reverse("lift_plan_app_planSketch_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_planSketch_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    url = reverse("lift_plan_app_planSketch_create")
    data = {
        "type": "text",
        "label": "text",
        "file_name": "aFile",
        "file_path": "aFile",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_planSketch_detail_view(client):
    instance = test_helpers.create_lift_plan_app_planSketch()
    url = reverse("lift_plan_app_planSketch_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_planSketch_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    instance = test_helpers.create_lift_plan_app_planSketch()
    url = reverse("lift_plan_app_planSketch_update", args=[instance.pk, ])
    data = {
        "type": "text",
        "label": "text",
        "file_name": "aFile",
        "file_path": "aFile",
        "form_id": form_id.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_workAssignment_list_view(client):
    instance1 = test_helpers.create_lift_plan_app_workAssignment()
    instance2 = test_helpers.create_lift_plan_app_workAssignment()
    url = reverse("lift_plan_app_workAssignment_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_workAssignment_create_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    lift_personal_flm = test_helpers.create_User()
    lift_personal_signaler = test_helpers.create_User()
    lift_personal_crane_operator = test_helpers.create_User()
    lift_personal_rigger = test_helpers.create_User()
    lift_personal_other_member_2 = test_helpers.create_User()
    lift_personal_other_member_1 = test_helpers.create_User()
    lift_personal_supervisior = test_helpers.create_User()
    url = reverse("lift_plan_app_workAssignment_create")
    data = {
        "supervisor_work_assignment_accept": True,
        "flm_work_assignment_accept": True,
        "work_date": datetime.now(),
        "work_id": "text",
        "flm_work_assignment_accept_date": datetime.now(),
        "supervisor_work_assignment_accept_date": datetime.now(),
        "form_id": form_id.pk,
        "lift_personal_flm": lift_personal_flm.pk,
        "lift_personal_signaler": lift_personal_signaler.pk,
        "lift_personal_crane_operator": lift_personal_crane_operator.pk,
        "lift_personal_rigger": lift_personal_rigger.pk,
        "lift_personal_other_member_2": lift_personal_other_member_2.pk,
        "lift_personal_other_member_1": lift_personal_other_member_1.pk,
        "lift_personal_supervisior": lift_personal_supervisior.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_workAssignment_detail_view(client):
    instance = test_helpers.create_lift_plan_app_workAssignment()
    url = reverse("lift_plan_app_workAssignment_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_workAssignment_update_view(client):
    form_id = test_helpers.create_lift_plan_app_planForm()
    lift_personal_flm = test_helpers.create_User()
    lift_personal_signaler = test_helpers.create_User()
    lift_personal_crane_operator = test_helpers.create_User()
    lift_personal_rigger = test_helpers.create_User()
    lift_personal_other_member_2 = test_helpers.create_User()
    lift_personal_other_member_1 = test_helpers.create_User()
    lift_personal_supervisior = test_helpers.create_User()
    instance = test_helpers.create_lift_plan_app_workAssignment()
    url = reverse("lift_plan_app_workAssignment_update", args=[instance.pk, ])
    data = {
        "supervisor_work_assignment_accept": True,
        "flm_work_assignment_accept": True,
        "work_date": datetime.now(),
        "work_id": "text",
        "flm_work_assignment_accept_date": datetime.now(),
        "supervisor_work_assignment_accept_date": datetime.now(),
        "form_id": form_id.pk,
        "lift_personal_flm": lift_personal_flm.pk,
        "lift_personal_signaler": lift_personal_signaler.pk,
        "lift_personal_crane_operator": lift_personal_crane_operator.pk,
        "lift_personal_rigger": lift_personal_rigger.pk,
        "lift_personal_other_member_2": lift_personal_other_member_2.pk,
        "lift_personal_other_member_1": lift_personal_other_member_1.pk,
        "lift_personal_supervisior": lift_personal_supervisior.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

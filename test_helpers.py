import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from page_management import models as page_management_models
from lift_plan_app import models as lift_plan_app_models
from organization_management import models as organization_management_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_page_management_Pages(**kwargs):
    defaults = {}
    defaults["publish_down"] = datetime.now()
    defaults["slug"] = ""
    defaults["page_title"] = ""
    defaults["publish"] = datetime.now()
    defaults["is_active"] = ""
    defaults["is_home_page"] = ""
    defaults["page_content"] = ""
    defaults["content_type"] = ""
    if "users" not in kwargs:
        defaults["users"] = create_User()
    if "groups" not in kwargs:
        defaults["groups"] = create_Group()
    defaults.update(**kwargs)
    return page_management_models.Pages.objects.create(**defaults)
def create_lift_plan_app_equipmentsList(**kwargs):
    defaults = {}
    defaults["type"] = ""
    defaults["capacity"] = ""
    defaults["tension"] = ""
    defaults["description"] = ""
    defaults["weight"] = ""
    defaults["tool_number"] = ""
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    defaults.update(**kwargs)
    return lift_plan_app_models.equipmentsList.objects.create(**defaults)
def create_lift_plan_app_liftDescriptions(**kwargs):
    defaults = {}
    defaults["load_items"] = ""
    defaults["load_centre"] = ""
    defaults["load_weight"] = ""
    defaults["total_weight"] = ""
    defaults["estimation"] = ""
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    defaults.update(**kwargs)
    return lift_plan_app_models.liftDescriptions.objects.create(**defaults)
def create_lift_plan_app_mobileCrane(**kwargs):
    defaults = {}
    defaults["crane_type"] = ""
    defaults["block_ball_size"] = ""
    defaults["boom_sections"] = ""
    defaults["manufacturer_restrictions"] = ""
    defaults["parts_of_line"] = ""
    defaults["capacity"] = ""
    defaults["manufacturer"] = ""
    defaults["equipment_number"] = ""
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    defaults.update(**kwargs)
    return lift_plan_app_models.mobileCrane.objects.create(**defaults)
def create_lift_plan_app_overheadCrane(**kwargs):
    defaults = {}
    defaults["equipment_code"] = ""
    defaults["auxiliary_hook_capacity"] = ""
    defaults["equipment_name"] = ""
    defaults["main_hook_capacity"] = ""
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    defaults.update(**kwargs)
    return lift_plan_app_models.overheadCrane.objects.create(**defaults)
def create_lift_plan_app_planAttachment(**kwargs):
    defaults = {}
    defaults["file_path"] = ""
    defaults["file_attachment"] = ""
    defaults["label"] = ""
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    defaults.update(**kwargs)
    return lift_plan_app_models.planAttachment.objects.create(**defaults)
def create_lift_plan_app_planForm(**kwargs):
    defaults = {}
    defaults["reason_for_lift"] = ""
    defaults["hazardous_or_toxic"] = ""
    defaults["usi_sci"] = ""
    defaults["equipment"] = ""
    defaults["form_status"] = ""
    defaults["swp_jsa"] = ""
    defaults["special_instructions"] = ""
    if "reviewed_by" not in kwargs:
        defaults["reviewed_by"] = create_User()
    if "prepared_by" not in kwargs:
        defaults["prepared_by"] = create_User()
    if "approved_by" not in kwargs:
        defaults["approved_by"] = create_User()
    defaults.update(**kwargs)
    return lift_plan_app_models.planForm.objects.create(**defaults)
def create_lift_plan_app_planSketch(**kwargs):
    defaults = {}
    defaults["type"] = ""
    defaults["label"] = ""
    defaults["file_name"] = ""
    defaults["file_path"] = ""
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    defaults.update(**kwargs)
    return lift_plan_app_models.planSketch.objects.create(**defaults)
def create_lift_plan_app_workAssignment(**kwargs):
    defaults = {}
    defaults["supervisor_work_assignment_accept"] = ""
    defaults["flm_work_assignment_accept"] = ""
    defaults["work_date"] = datetime.now()
    defaults["work_id"] = ""
    defaults["flm_work_assignment_accept_date"] = datetime.now()
    defaults["supervisor_work_assignment_accept_date"] = datetime.now()
    if "form_id" not in kwargs:
        defaults["form_id"] = create_lift_plan_app_planForm()
    if "lift_personal_flm" not in kwargs:
        defaults["lift_personal_flm"] = create_User()
    if "lift_personal_signaler" not in kwargs:
        defaults["lift_personal_signaler"] = create_User()
    if "lift_personal_crane_operator" not in kwargs:
        defaults["lift_personal_crane_operator"] = create_User()
    if "lift_personal_rigger" not in kwargs:
        defaults["lift_personal_rigger"] = create_User()
    if "lift_personal_other_member_2" not in kwargs:
        defaults["lift_personal_other_member_2"] = create_User()
    if "lift_personal_other_member_1" not in kwargs:
        defaults["lift_personal_other_member_1"] = create_User()
    if "lift_personal_supervisior" not in kwargs:
        defaults["lift_personal_supervisior"] = create_User()
    defaults.update(**kwargs)
    return lift_plan_app_models.workAssignment.objects.create(**defaults)
def create_organization_management_User(**kwargs):
    defaults = {}
    defaults["reporting_manager_name"] = ""
    defaults["reporting_manager_email"] = ""
    defaults["first_time_login"] = ""
    defaults["signature"] = ""
    defaults["reporting_manager_uuid"] = ""
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return organization_management_models.User.objects.create(**defaults)

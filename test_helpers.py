import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType

from hoisting_rigging_app import models as hoisting_rigging_app_models


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


def create_hoisting_rigging_app_appForm(**kwargs):
    defaults = {}
    defaults["special_instructions"] = ""
    defaults["form_type"] = ""
    defaults["form_status"] = ""
    defaults["lift_plan_sketch_description"] = ""
    defaults["lift_plan_sketch_image"] = ""
    defaults["reason"] = ""
    defaults["equipment"] = ""
    defaults["floor_plan_sketch_image"] = ""
    defaults["swp_jsa"] = ""
    defaults["floor_plan_sketch_description"] = ""
    defaults["usi_sci"] = ""
    defaults["hazardous_toxic_material"] = ""
    if "reviewed_by" not in kwargs:
        defaults["reviewed_by"] = create_User()
    if "approved_by" not in kwargs:
        defaults["approved_by"] = create_User()
    if "crane_operator" not in kwargs:
        defaults["crane_operator"] = create_User()
    if "rigger" not in kwargs:
        defaults["rigger"] = create_User()
    if "flm" not in kwargs:
        defaults["flm"] = create_User()
    if "signaler" not in kwargs:
        defaults["signaler"] = create_User()
    if "supervisor_of_lift" not in kwargs:
        defaults["supervisor_of_lift"] = create_User()
    if "prepared_by" not in kwargs:
        defaults["prepared_by"] = create_User()
    if "other" not in kwargs:
        defaults["other"] = create_User()
    defaults.update(**kwargs)
    return hoisting_rigging_app_models.appForm.objects.create(**defaults)
def create_hoisting_rigging_app_liftDescription(**kwargs):
    defaults = {}
    defaults["estimate_calculated_measured"] = ""
    defaults["c_of_g_12_of_load_centre"] = ""
    defaults["load_weight"] = ""
    defaults["load_items"] = ""
    defaults["total_weight"] = ""
    if "appFormId" not in kwargs:
        defaults["appFormId"] = create_hoisting_rigging_app_appForm()
    defaults.update(**kwargs)
    return hoisting_rigging_app_models.liftDescription.objects.create(**defaults)
def create_hoisting_rigging_app_mobileCrane(**kwargs):
    defaults = {}
    defaults["parts_of_line"] = ""
    defaults["capacity"] = ""
    defaults["equipment_number"] = ""
    defaults["block_ball_size"] = ""
    defaults["crane_type"] = ""
    defaults["boom_sections"] = ""
    defaults["manufacturer"] = ""
    if "appFormId" not in kwargs:
        defaults["appFormId"] = create_hoisting_rigging_app_appForm()
    defaults.update(**kwargs)
    return hoisting_rigging_app_models.mobileCrane.objects.create(**defaults)
def create_hoisting_rigging_app_overheadCrane(**kwargs):
    defaults = {}
    defaults["equipment_name"] = ""
    defaults["equipment_code"] = ""
    defaults["auxiliary_hook_capacity"] = ""
    defaults["main_hook_capacity"] = ""
    if "appFormId" not in kwargs:
        defaults["appFormId"] = create_hoisting_rigging_app_appForm()
    defaults.update(**kwargs)
    return hoisting_rigging_app_models.overheadCrane.objects.create(**defaults)
def create_hoisting_rigging_app_tools_hardware(**kwargs):
    defaults = {}
    defaults["capacity"] = ""
    defaults["weight"] = ""
    defaults["tool_number"] = ""
    defaults["description"] = ""
    defaults["tension"] = ""
    defaults["type"] = ""
    defaults["quantity"] = ""
    if "appFormId" not in kwargs:
        defaults["appFormId"] = create_hoisting_rigging_app_appForm()
    defaults.update(**kwargs)
    return hoisting_rigging_app_models.tools_hardware.objects.create(**defaults)

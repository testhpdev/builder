from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from hoisting_rigging_app.models import appForm
from hoisting_rigging_app.models import appForm
from hoisting_rigging_app.models import appForm
from hoisting_rigging_app.models import appForm
from . import models


class appFormForm(forms.ModelForm):
    class Meta:
        model = models.appForm
        fields = [
            "special_instructions",
            "form_type",
            "form_status",
            "lift_plan_sketch_description",
            "lift_plan_sketch_image",
            "reason",
            "equipment",
            "floor_plan_sketch_image",
            "swp_jsa",
            "floor_plan_sketch_description",
            "usi_sci",
            "hazardous_toxic_material",
            "reviewed_by",
            "approved_by",
            "crane_operator",
            "rigger",
            "flm",
            "signaler",
            "supervisor_of_lift",
            "prepared_by",
            "other",
        ]

    def __init__(self, *args, **kwargs):
        super(appFormForm, self).__init__(*args, **kwargs)
        self.fields["reviewed_by"].queryset = User.objects.all()
        self.fields["approved_by"].queryset = User.objects.all()
        self.fields["crane_operator"].queryset = User.objects.all()
        self.fields["rigger"].queryset = User.objects.all()
        self.fields["flm"].queryset = User.objects.all()
        self.fields["signaler"].queryset = User.objects.all()
        self.fields["supervisor_of_lift"].queryset = User.objects.all()
        self.fields["prepared_by"].queryset = User.objects.all()
        self.fields["other"].queryset = User.objects.all()



class liftDescriptionForm(forms.ModelForm):
    class Meta:
        model = models.liftDescription
        fields = [
            "estimate_calculated_measured",
            "c_of_g_12_of_load_centre",
            "load_weight",
            "load_items",
            "total_weight",
            "appFormId",
        ]

    def __init__(self, *args, **kwargs):
        super(liftDescriptionForm, self).__init__(*args, **kwargs)
        self.fields["appFormId"].queryset = appForm.objects.all()



class mobileCraneForm(forms.ModelForm):
    class Meta:
        model = models.mobileCrane
        fields = [
            "parts_of_line",
            "capacity",
            "equipment_number",
            "block_ball_size",
            "crane_type",
            "boom_sections",
            "manufacturer",
            "appFormId",
        ]

    def __init__(self, *args, **kwargs):
        super(mobileCraneForm, self).__init__(*args, **kwargs)
        self.fields["appFormId"].queryset = appForm.objects.all()



class overheadCraneForm(forms.ModelForm):
    class Meta:
        model = models.overheadCrane
        fields = [
            "equipment_name",
            "equipment_code",
            "auxiliary_hook_capacity",
            "main_hook_capacity",
            "appFormId",
        ]

    def __init__(self, *args, **kwargs):
        super(overheadCraneForm, self).__init__(*args, **kwargs)
        self.fields["appFormId"].queryset = appForm.objects.all()



class tools_hardwareForm(forms.ModelForm):
    class Meta:
        model = models.tools_hardware
        fields = [
            "capacity",
            "weight",
            "tool_number",
            "description",
            "tension",
            "type",
            "quantity",
            "appFormId",
        ]

    def __init__(self, *args, **kwargs):
        super(tools_hardwareForm, self).__init__(*args, **kwargs)
        self.fields["appFormId"].queryset = appForm.objects.all()


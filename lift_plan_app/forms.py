from django import forms
from lift_plan_app.models import planForm
from lift_plan_app.models import planForm
from lift_plan_app.models import planForm
from lift_plan_app.models import planForm
from lift_plan_app.models import planForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from lift_plan_app.models import planForm
from lift_plan_app.models import planForm
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from . import models


class equipmentsListForm(forms.ModelForm):
    class Meta:
        model = models.equipmentsList
        fields = [
            "type",
            "capacity",
            "tension",
            "description",
            "weight",
            "tool_number",
            "form_id",
        ]

    def __init__(self, *args, **kwargs):
        super(equipmentsListForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()



class liftDescriptionsForm(forms.ModelForm):
    class Meta:
        model = models.liftDescriptions
        fields = [
            "load_items",
            "load_centre",
            "load_weight",
            "total_weight",
            "estimation",
            "form_id",
        ]

    def __init__(self, *args, **kwargs):
        super(liftDescriptionsForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()



class mobileCraneForm(forms.ModelForm):
    class Meta:
        model = models.mobileCrane
        fields = [
            "crane_type",
            "block_ball_size",
            "boom_sections",
            "manufacturer_restrictions",
            "parts_of_line",
            "capacity",
            "manufacturer",
            "equipment_number",
            "form_id",
        ]

    def __init__(self, *args, **kwargs):
        super(mobileCraneForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()



class overheadCraneForm(forms.ModelForm):
    class Meta:
        model = models.overheadCrane
        fields = [
            "equipment_code",
            "auxiliary_hook_capacity",
            "equipment_name",
            "main_hook_capacity",
            "form_id",
        ]

    def __init__(self, *args, **kwargs):
        super(overheadCraneForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()



class planAttachmentForm(forms.ModelForm):
    class Meta:
        model = models.planAttachment
        fields = [
            "file_path",
            "file_attachment",
            "label",
            "form_id",
        ]

    def __init__(self, *args, **kwargs):
        super(planAttachmentForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()



class planFormForm(forms.ModelForm):
    class Meta:
        model = models.planForm
        fields = [
            "reason_for_lift",
            "hazardous_or_toxic",
            "usi_sci",
            "equipment",
            "form_status",
            "swp_jsa",
            "special_instructions",
            "reviewed_by",
            "prepared_by",
            "approved_by",
        ]

    def __init__(self, *args, **kwargs):
        super(planFormForm, self).__init__(*args, **kwargs)
        self.fields["reviewed_by"].queryset = User.objects.all()
        self.fields["prepared_by"].queryset = User.objects.all()
        self.fields["approved_by"].queryset = User.objects.all()



class planSketchForm(forms.ModelForm):
    class Meta:
        model = models.planSketch
        fields = [
            "type",
            "label",
            "file_name",
            "file_path",
            "form_id",
        ]

    def __init__(self, *args, **kwargs):
        super(planSketchForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()



class workAssignmentForm(forms.ModelForm):
    class Meta:
        model = models.workAssignment
        fields = [
            "supervisor_work_assignment_accept",
            "flm_work_assignment_accept",
            "work_date",
            "work_id",
            "flm_work_assignment_accept_date",
            "supervisor_work_assignment_accept_date",
            "form_id",
            "lift_personal_flm",
            "lift_personal_signaler",
            "lift_personal_crane_operator",
            "lift_personal_rigger",
            "lift_personal_other_member_2",
            "lift_personal_other_member_1",
            "lift_personal_supervisior",
        ]

    def __init__(self, *args, **kwargs):
        super(workAssignmentForm, self).__init__(*args, **kwargs)
        self.fields["form_id"].queryset = planForm.objects.all()
        self.fields["lift_personal_flm"].queryset = User.objects.all()
        self.fields["lift_personal_signaler"].queryset = User.objects.all()
        self.fields["lift_personal_crane_operator"].queryset = User.objects.all()
        self.fields["lift_personal_rigger"].queryset = User.objects.all()
        self.fields["lift_personal_other_member_2"].queryset = User.objects.all()
        self.fields["lift_personal_other_member_1"].queryset = User.objects.all()
        self.fields["lift_personal_supervisior"].queryset = User.objects.all()


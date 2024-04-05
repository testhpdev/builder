from django.contrib import admin
from django import forms

from . import models


class equipmentsListAdminForm(forms.ModelForm):

    class Meta:
        model = models.equipmentsList
        fields = "__all__"


class equipmentsListAdmin(admin.ModelAdmin):
    form = equipmentsListAdminForm
    list_display = [
        "id",
        "last_updated",
        "type",
        "capacity",
        "created",
        "tension",
        "description",
        "weight",
        "tool_number",
    ]
    readonly_fields = [
        "id",
        "last_updated",
        "type",
        "capacity",
        "created",
        "tension",
        "description",
        "weight",
        "tool_number",
    ]


class liftDescriptionsAdminForm(forms.ModelForm):

    class Meta:
        model = models.liftDescriptions
        fields = "__all__"


class liftDescriptionsAdmin(admin.ModelAdmin):
    form = liftDescriptionsAdminForm
    list_display = [
        "load_items",
        "load_centre",
        "last_updated",
        "id",
        "load_weight",
        "created",
        "total_weight",
        "estimation",
    ]
    readonly_fields = [
        "load_items",
        "load_centre",
        "last_updated",
        "id",
        "load_weight",
        "created",
        "total_weight",
        "estimation",
    ]


class mobileCraneAdminForm(forms.ModelForm):

    class Meta:
        model = models.mobileCrane
        fields = "__all__"


class mobileCraneAdmin(admin.ModelAdmin):
    form = mobileCraneAdminForm
    list_display = [
        "crane_type",
        "block_ball_size",
        "boom_sections",
        "created",
        "manufacturer_restrictions",
        "parts_of_line",
        "capacity",
        "last_updated",
        "manufacturer",
        "id",
        "equipment_number",
    ]
    readonly_fields = [
        "crane_type",
        "block_ball_size",
        "boom_sections",
        "created",
        "manufacturer_restrictions",
        "parts_of_line",
        "capacity",
        "last_updated",
        "manufacturer",
        "id",
        "equipment_number",
    ]


class overheadCraneAdminForm(forms.ModelForm):

    class Meta:
        model = models.overheadCrane
        fields = "__all__"


class overheadCraneAdmin(admin.ModelAdmin):
    form = overheadCraneAdminForm
    list_display = [
        "last_updated",
        "equipment_code",
        "id",
        "auxiliary_hook_capacity",
        "equipment_name",
        "main_hook_capacity",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "equipment_code",
        "id",
        "auxiliary_hook_capacity",
        "equipment_name",
        "main_hook_capacity",
        "created",
    ]


class planAttachmentAdminForm(forms.ModelForm):

    class Meta:
        model = models.planAttachment
        fields = "__all__"


class planAttachmentAdmin(admin.ModelAdmin):
    form = planAttachmentAdminForm
    list_display = [
        "id",
        "file_path",
        "file_attachment",
        "last_updated",
        "created",
        "label",
    ]
    readonly_fields = [
        "id",
        "file_path",
        "file_attachment",
        "last_updated",
        "created",
        "label",
    ]


class planFormAdminForm(forms.ModelForm):

    class Meta:
        model = models.planForm
        fields = "__all__"


class planFormAdmin(admin.ModelAdmin):
    form = planFormAdminForm
    list_display = [
        "reason_for_lift",
        "hazardous_or_toxic",
        "id",
        "usi_sci",
        "equipment",
        "last_updated",
        "created",
        "form_status",
        "swp_jsa",
        "special_instructions",
    ]
    readonly_fields = [
        "reason_for_lift",
        "hazardous_or_toxic",
        "id",
        "usi_sci",
        "equipment",
        "last_updated",
        "created",
        "form_status",
        "swp_jsa",
        "special_instructions",
    ]


class planSketchAdminForm(forms.ModelForm):

    class Meta:
        model = models.planSketch
        fields = "__all__"


class planSketchAdmin(admin.ModelAdmin):
    form = planSketchAdminForm
    list_display = [
        "type",
        "label",
        "last_updated",
        "file_name",
        "id",
        "created",
        "file_path",
    ]
    readonly_fields = [
        "type",
        "label",
        "last_updated",
        "file_name",
        "id",
        "created",
        "file_path",
    ]


class workAssignmentAdminForm(forms.ModelForm):

    class Meta:
        model = models.workAssignment
        fields = "__all__"


class workAssignmentAdmin(admin.ModelAdmin):
    form = workAssignmentAdminForm
    list_display = [
        "supervisor_work_assignment_accept",
        "flm_work_assignment_accept",
        "work_date",
        "last_updated",
        "work_id",
        "flm_work_assignment_accept_date",
        "supervisor_work_assignment_accept_date",
        "created",
        "id",
    ]
    readonly_fields = [
        "supervisor_work_assignment_accept",
        "flm_work_assignment_accept",
        "work_date",
        "last_updated",
        "work_id",
        "flm_work_assignment_accept_date",
        "supervisor_work_assignment_accept_date",
        "created",
        "id",
    ]


admin.site.register(models.equipmentsList, equipmentsListAdmin)
admin.site.register(models.liftDescriptions, liftDescriptionsAdmin)
admin.site.register(models.mobileCrane, mobileCraneAdmin)
admin.site.register(models.overheadCrane, overheadCraneAdmin)
admin.site.register(models.planAttachment, planAttachmentAdmin)
admin.site.register(models.planForm, planFormAdmin)
admin.site.register(models.planSketch, planSketchAdmin)
admin.site.register(models.workAssignment, workAssignmentAdmin)

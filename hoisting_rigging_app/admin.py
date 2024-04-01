from django.contrib import admin
from django import forms

from . import models


class appFormAdminForm(forms.ModelForm):

    class Meta:
        model = models.appForm
        fields = "__all__"


class appFormAdmin(admin.ModelAdmin):
    form = appFormAdminForm
    list_display = [
        "special_instructions",
        "form_type",
        "id",
        "form_status",
        "lift_plan_sketch_description",
        "last_updated",
        "lift_plan_sketch_image",
        "reason",
        "equipment",
        "floor_plan_sketch_image",
        "swp_jsa",
        "floor_plan_sketch_description",
        "usi_sci",
        "created",
        "hazardous_toxic_material",
    ]
    readonly_fields = [
        "special_instructions",
        "form_type",
        "id",
        "form_status",
        "lift_plan_sketch_description",
        "last_updated",
        "lift_plan_sketch_image",
        "reason",
        "equipment",
        "floor_plan_sketch_image",
        "swp_jsa",
        "floor_plan_sketch_description",
        "usi_sci",
        "created",
        "hazardous_toxic_material",
    ]


class liftDescriptionAdminForm(forms.ModelForm):

    class Meta:
        model = models.liftDescription
        fields = "__all__"


class liftDescriptionAdmin(admin.ModelAdmin):
    form = liftDescriptionAdminForm
    list_display = [
        "estimate_calculated_measured",
        "id",
        "c_of_g_12_of_load_centre",
        "load_weight",
        "load_items",
        "total_weight",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "estimate_calculated_measured",
        "id",
        "c_of_g_12_of_load_centre",
        "load_weight",
        "load_items",
        "total_weight",
        "created",
        "last_updated",
    ]


class mobileCraneAdminForm(forms.ModelForm):

    class Meta:
        model = models.mobileCrane
        fields = "__all__"


class mobileCraneAdmin(admin.ModelAdmin):
    form = mobileCraneAdminForm
    list_display = [
        "id",
        "last_updated",
        "parts_of_line",
        "capacity",
        "created",
        "equipment_number",
        "block_ball_size",
        "crane_type",
        "boom_sections",
        "manufacturer",
    ]
    readonly_fields = [
        "id",
        "last_updated",
        "parts_of_line",
        "capacity",
        "created",
        "equipment_number",
        "block_ball_size",
        "crane_type",
        "boom_sections",
        "manufacturer",
    ]


class overheadCraneAdminForm(forms.ModelForm):

    class Meta:
        model = models.overheadCrane
        fields = "__all__"


class overheadCraneAdmin(admin.ModelAdmin):
    form = overheadCraneAdminForm
    list_display = [
        "equipment_name",
        "last_updated",
        "created",
        "id",
        "equipment_code",
        "auxiliary_hook_capacity",
        "main_hook_capacity",
    ]
    readonly_fields = [
        "equipment_name",
        "last_updated",
        "created",
        "id",
        "equipment_code",
        "auxiliary_hook_capacity",
        "main_hook_capacity",
    ]


class tools_hardwareAdminForm(forms.ModelForm):

    class Meta:
        model = models.tools_hardware
        fields = "__all__"


class tools_hardwareAdmin(admin.ModelAdmin):
    form = tools_hardwareAdminForm
    list_display = [
        "capacity",
        "last_updated",
        "weight",
        "tool_number",
        "description",
        "tension",
        "created",
        "id",
        "type",
        "quantity",
    ]
    readonly_fields = [
        "capacity",
        "last_updated",
        "weight",
        "tool_number",
        "description",
        "tension",
        "created",
        "id",
        "type",
        "quantity",
    ]


admin.site.register(models.appForm, appFormAdmin)
admin.site.register(models.liftDescription, liftDescriptionAdmin)
admin.site.register(models.mobileCrane, mobileCraneAdmin)
admin.site.register(models.overheadCrane, overheadCraneAdmin)
admin.site.register(models.tools_hardware, tools_hardwareAdmin)

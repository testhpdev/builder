from rest_framework import serializers

from . import models


class appFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.appForm
        fields = [
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

class liftDescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.liftDescription
        fields = [
            "estimate_calculated_measured",
            "id",
            "c_of_g_12_of_load_centre",
            "load_weight",
            "load_items",
            "total_weight",
            "created",
            "last_updated",
            "appFormId",
        ]

class mobileCraneSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.mobileCrane
        fields = [
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
            "appFormId",
        ]

class overheadCraneSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.overheadCrane
        fields = [
            "equipment_name",
            "last_updated",
            "created",
            "id",
            "equipment_code",
            "auxiliary_hook_capacity",
            "main_hook_capacity",
            "appFormId",
        ]

class tools_hardwareSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.tools_hardware
        fields = [
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
            "appFormId",
        ]

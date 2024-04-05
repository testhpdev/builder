from rest_framework import serializers

from . import models


class equipmentsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.equipmentsList
        fields = [
            "id",
            "last_updated",
            "type",
            "capacity",
            "created",
            "tension",
            "description",
            "weight",
            "tool_number",
            "form_id",
        ]

class liftDescriptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.liftDescriptions
        fields = [
            "load_items",
            "load_centre",
            "last_updated",
            "id",
            "load_weight",
            "created",
            "total_weight",
            "estimation",
            "form_id",
        ]

class mobileCraneSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.mobileCrane
        fields = [
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
            "form_id",
        ]

class overheadCraneSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.overheadCrane
        fields = [
            "last_updated",
            "equipment_code",
            "id",
            "auxiliary_hook_capacity",
            "equipment_name",
            "main_hook_capacity",
            "created",
            "form_id",
        ]

class planAttachmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.planAttachment
        fields = [
            "id",
            "file_path",
            "file_attachment",
            "last_updated",
            "created",
            "label",
            "form_id",
        ]

class planFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.planForm
        fields = [
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
            "reviewed_by",
            "prepared_by",
            "approved_by",
        ]

class planSketchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.planSketch
        fields = [
            "type",
            "label",
            "last_updated",
            "file_name",
            "id",
            "created",
            "file_path",
            "form_id",
        ]

class workAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.workAssignment
        fields = [
            "supervisor_work_assignment_accept",
            "flm_work_assignment_accept",
            "work_date",
            "last_updated",
            "work_id",
            "flm_work_assignment_accept_date",
            "supervisor_work_assignment_accept_date",
            "created",
            "id",
            "form_id",
            "lift_personal_flm",
            "lift_personal_signaler",
            "lift_personal_crane_operator",
            "lift_personal_rigger",
            "lift_personal_other_member_2",
            "lift_personal_other_member_1",
            "lift_personal_supervisior",
        ]

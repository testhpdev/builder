from django.db import models
from django.urls import reverse


class equipmentsList(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    type = models.CharField(max_length=30)
    capacity = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    tension = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    weight = models.CharField(max_length=30)
    tool_number = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_equipmentsList_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_equipmentsList_update", args=(self.pk,))



class liftDescriptions(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)

    # Fields
    load_items = models.CharField(max_length=300)
    load_centre = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    load_weight = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    total_weight = models.CharField(max_length=300)
    estimation = models.CharField(max_length=300)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_liftDescriptions_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_liftDescriptions_update", args=(self.pk,))



class mobileCrane(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)

    # Fields
    crane_type = models.CharField(max_length=30)
    block_ball_size = models.CharField(max_length=100)
    boom_sections = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    manufacturer_restrictions = models.TextField()
    parts_of_line = models.CharField(max_length=100)
    capacity = models.CharField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    manufacturer = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment_number = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_mobileCrane_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_mobileCrane_update", args=(self.pk,))



class overheadCrane(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    equipment_code = models.CharField(max_length=50)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auxiliary_hook_capacity = models.CharField(max_length=100)
    equipment_name = models.CharField(max_length=100)
    main_hook_capacity = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_overheadCrane_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_overheadCrane_update", args=(self.pk,))



class planAttachment(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file_path = models.FilePathField()
    file_attachment = models.FileField(upload_to="media/upload/lift_plan_attachment/")
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    label = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_planAttachment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_planAttachment_update", args=(self.pk,))



class planForm(models.Model):

    # Relationships
    reviewed_by = models.OneToOneField("auth.User", on_delete=models.DO_NOTHING)
    prepared_by = models.OneToOneField("auth.User", on_delete=models.DO_NOTHING)
    approved_by = models.OneToOneField("auth.User", on_delete=models.DO_NOTHING)

    # Fields
    reason_for_lift = models.TextField()
    hazardous_or_toxic = models.BooleanField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usi_sci = models.CharField(max_length=300)
    equipment = models.CharField(max_length=300)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    form_status = models.CharField(max_length=30)
    swp_jsa = models.CharField(max_length=300)
    special_instructions = models.TextField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_planForm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_planForm_update", args=(self.pk,))



class planSketch(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)

    # Fields
    type = models.CharField(max_length=30)
    label = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    file_name = models.FileField(upload_to="media/upload/lift_plan/")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    file_path = models.FilePathField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_planSketch_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_planSketch_update", args=(self.pk,))



class workAssignment(models.Model):

    # Relationships
    form_id = models.ForeignKey("lift_plan_app.planForm", on_delete=models.DO_NOTHING)
    lift_personal_flm = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    lift_personal_signaler = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    lift_personal_crane_operator = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    lift_personal_rigger = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    lift_personal_other_member_2 = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    lift_personal_other_member_1 = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)
    lift_personal_supervisior = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING)

    # Fields
    supervisor_work_assignment_accept = models.NullBooleanField()
    flm_work_assignment_accept = models.NullBooleanField()
    work_date = models.DateField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    work_id = models.CharField(max_length=30)
    flm_work_assignment_accept_date = models.DateField()
    supervisor_work_assignment_accept_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("lift_plan_app_workAssignment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("lift_plan_app_workAssignment_update", args=(self.pk,))


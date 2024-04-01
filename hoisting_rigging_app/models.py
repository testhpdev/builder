from django.db import models
from django.urls import reverse


class appForm(models.Model):

    # Relationships
    reviewed_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    approved_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    crane_operator = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    rigger = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    flm = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    signaler = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    supervisor_of_lift = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    prepared_by = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    other = models.ManyToManyField("auth.User")

    # Fields
    special_instructions = models.TextField()
    form_type = models.CharField(max_length=10)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    form_status = models.TextField(max_length=10)
    lift_plan_sketch_description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    lift_plan_sketch_image = models.ImageField(upload_to="upload/images/lift_plan_sketch")
    reason = models.TextField()
    equipment = models.TextField(max_length=255)
    floor_plan_sketch_image = models.ImageField(upload_to="upload/images/floor_plan")
    swp_jsa = models.TextField(max_length=255)
    floor_plan_sketch_description = models.TextField()
    usi_sci = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    hazardous_toxic_material = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("hoisting_rigging_app_appForm_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("hoisting_rigging_app_appForm_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("hoisting_rigging_app_appForm_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("hoisting_rigging_app_appForm_htmx_delete", args=(self.pk,))


class liftDescription(models.Model):

    # Relationships
    appFormId = models.ForeignKey("hoisting_rigging_app.appForm", on_delete=models.CASCADE)

    # Fields
    estimate_calculated_measured = models.TextField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    c_of_g_12_of_load_centre = models.NullBooleanField()
    load_weight = models.TextField(max_length=100)
    load_items = models.TextField(max_length=255)
    total_weight = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("hoisting_rigging_app_liftDescription_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("hoisting_rigging_app_liftDescription_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("hoisting_rigging_app_liftDescription_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("hoisting_rigging_app_liftDescription_htmx_delete", args=(self.pk,))


class mobileCrane(models.Model):

    # Relationships
    appFormId = models.ForeignKey("hoisting_rigging_app.appForm", on_delete=models.CASCADE)

    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    parts_of_line = models.TextField(max_length=100)
    capacity = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    equipment_number = models.TextField(max_length=100)
    block_ball_size = models.TextField(max_length=100)
    crane_type = models.TextField(max_length=100)
    boom_sections = models.TextField(max_length=100)
    manufacturer = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("hoisting_rigging_app_mobileCrane_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("hoisting_rigging_app_mobileCrane_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("hoisting_rigging_app_mobileCrane_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("hoisting_rigging_app_mobileCrane_htmx_delete", args=(self.pk,))


class overheadCrane(models.Model):

    # Relationships
    appFormId = models.ForeignKey("hoisting_rigging_app.appForm", on_delete=models.CASCADE)

    # Fields
    equipment_name = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    equipment_code = models.TextField(max_length=100)
    auxiliary_hook_capacity = models.TextField(max_length=100)
    main_hook_capacity = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("hoisting_rigging_app_overheadCrane_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("hoisting_rigging_app_overheadCrane_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("hoisting_rigging_app_overheadCrane_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("hoisting_rigging_app_overheadCrane_htmx_delete", args=(self.pk,))


class tools_hardware(models.Model):

    # Relationships
    appFormId = models.ForeignKey("hoisting_rigging_app.appForm", on_delete=models.CASCADE)

    # Fields
    capacity = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    weight = models.TextField(max_length=100)
    tool_number = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    tension = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.TextField(max_length=100)
    quantity = models.IntegerField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("hoisting_rigging_app_tools_hardware_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("hoisting_rigging_app_tools_hardware_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("hoisting_rigging_app_tools_hardware_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("hoisting_rigging_app_tools_hardware_htmx_delete", args=(self.pk,))

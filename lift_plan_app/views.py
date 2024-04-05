from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class equipmentsListListView(generic.ListView):
    model = models.equipmentsList
    form_class = forms.equipmentsListForm


class equipmentsListCreateView(generic.CreateView):
    model = models.equipmentsList
    form_class = forms.equipmentsListForm


class equipmentsListDetailView(generic.DetailView):
    model = models.equipmentsList
    form_class = forms.equipmentsListForm


class equipmentsListUpdateView(generic.UpdateView):
    model = models.equipmentsList
    form_class = forms.equipmentsListForm
    pk_url_kwarg = "pk"


class equipmentsListDeleteView(generic.DeleteView):
    model = models.equipmentsList
    success_url = reverse_lazy("lift_plan_app_equipmentsList_list")


class liftDescriptionsListView(generic.ListView):
    model = models.liftDescriptions
    form_class = forms.liftDescriptionsForm


class liftDescriptionsCreateView(generic.CreateView):
    model = models.liftDescriptions
    form_class = forms.liftDescriptionsForm


class liftDescriptionsDetailView(generic.DetailView):
    model = models.liftDescriptions
    form_class = forms.liftDescriptionsForm


class liftDescriptionsUpdateView(generic.UpdateView):
    model = models.liftDescriptions
    form_class = forms.liftDescriptionsForm
    pk_url_kwarg = "pk"


class liftDescriptionsDeleteView(generic.DeleteView):
    model = models.liftDescriptions
    success_url = reverse_lazy("lift_plan_app_liftDescriptions_list")


class mobileCraneListView(generic.ListView):
    model = models.mobileCrane
    form_class = forms.mobileCraneForm


class mobileCraneCreateView(generic.CreateView):
    model = models.mobileCrane
    form_class = forms.mobileCraneForm


class mobileCraneDetailView(generic.DetailView):
    model = models.mobileCrane
    form_class = forms.mobileCraneForm


class mobileCraneUpdateView(generic.UpdateView):
    model = models.mobileCrane
    form_class = forms.mobileCraneForm
    pk_url_kwarg = "pk"


class mobileCraneDeleteView(generic.DeleteView):
    model = models.mobileCrane
    success_url = reverse_lazy("lift_plan_app_mobileCrane_list")


class overheadCraneListView(generic.ListView):
    model = models.overheadCrane
    form_class = forms.overheadCraneForm


class overheadCraneCreateView(generic.CreateView):
    model = models.overheadCrane
    form_class = forms.overheadCraneForm


class overheadCraneDetailView(generic.DetailView):
    model = models.overheadCrane
    form_class = forms.overheadCraneForm


class overheadCraneUpdateView(generic.UpdateView):
    model = models.overheadCrane
    form_class = forms.overheadCraneForm
    pk_url_kwarg = "pk"


class overheadCraneDeleteView(generic.DeleteView):
    model = models.overheadCrane
    success_url = reverse_lazy("lift_plan_app_overheadCrane_list")


class planAttachmentListView(generic.ListView):
    model = models.planAttachment
    form_class = forms.planAttachmentForm


class planAttachmentCreateView(generic.CreateView):
    model = models.planAttachment
    form_class = forms.planAttachmentForm


class planAttachmentDetailView(generic.DetailView):
    model = models.planAttachment
    form_class = forms.planAttachmentForm


class planAttachmentUpdateView(generic.UpdateView):
    model = models.planAttachment
    form_class = forms.planAttachmentForm
    pk_url_kwarg = "pk"


class planAttachmentDeleteView(generic.DeleteView):
    model = models.planAttachment
    success_url = reverse_lazy("lift_plan_app_planAttachment_list")


class planFormListView(generic.ListView):
    model = models.planForm
    form_class = forms.planFormForm


class planFormCreateView(generic.CreateView):
    model = models.planForm
    form_class = forms.planFormForm


class planFormDetailView(generic.DetailView):
    model = models.planForm
    form_class = forms.planFormForm


class planFormUpdateView(generic.UpdateView):
    model = models.planForm
    form_class = forms.planFormForm
    pk_url_kwarg = "pk"


class planFormDeleteView(generic.DeleteView):
    model = models.planForm
    success_url = reverse_lazy("lift_plan_app_planForm_list")


class planSketchListView(generic.ListView):
    model = models.planSketch
    form_class = forms.planSketchForm


class planSketchCreateView(generic.CreateView):
    model = models.planSketch
    form_class = forms.planSketchForm


class planSketchDetailView(generic.DetailView):
    model = models.planSketch
    form_class = forms.planSketchForm


class planSketchUpdateView(generic.UpdateView):
    model = models.planSketch
    form_class = forms.planSketchForm
    pk_url_kwarg = "pk"


class planSketchDeleteView(generic.DeleteView):
    model = models.planSketch
    success_url = reverse_lazy("lift_plan_app_planSketch_list")


class workAssignmentListView(generic.ListView):
    model = models.workAssignment
    form_class = forms.workAssignmentForm


class workAssignmentCreateView(generic.CreateView):
    model = models.workAssignment
    form_class = forms.workAssignmentForm


class workAssignmentDetailView(generic.DetailView):
    model = models.workAssignment
    form_class = forms.workAssignmentForm


class workAssignmentUpdateView(generic.UpdateView):
    model = models.workAssignment
    form_class = forms.workAssignmentForm
    pk_url_kwarg = "pk"


class workAssignmentDeleteView(generic.DeleteView):
    model = models.workAssignment
    success_url = reverse_lazy("lift_plan_app_workAssignment_list")

from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class appFormListView(generic.ListView):
    model = models.appForm
    form_class = forms.appFormForm


class appFormCreateView(generic.CreateView):
    model = models.appForm
    form_class = forms.appFormForm


class appFormDetailView(generic.DetailView):
    model = models.appForm
    form_class = forms.appFormForm


class appFormUpdateView(generic.UpdateView):
    model = models.appForm
    form_class = forms.appFormForm
    pk_url_kwarg = "pk"


class appFormDeleteView(generic.DeleteView):
    model = models.appForm
    success_url = reverse_lazy("hoisting_rigging_app_appForm_list")


class liftDescriptionListView(generic.ListView):
    model = models.liftDescription
    form_class = forms.liftDescriptionForm


class liftDescriptionCreateView(generic.CreateView):
    model = models.liftDescription
    form_class = forms.liftDescriptionForm


class liftDescriptionDetailView(generic.DetailView):
    model = models.liftDescription
    form_class = forms.liftDescriptionForm


class liftDescriptionUpdateView(generic.UpdateView):
    model = models.liftDescription
    form_class = forms.liftDescriptionForm
    pk_url_kwarg = "pk"


class liftDescriptionDeleteView(generic.DeleteView):
    model = models.liftDescription
    success_url = reverse_lazy("hoisting_rigging_app_liftDescription_list")


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
    success_url = reverse_lazy("hoisting_rigging_app_mobileCrane_list")


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
    success_url = reverse_lazy("hoisting_rigging_app_overheadCrane_list")


class tools_hardwareListView(generic.ListView):
    model = models.tools_hardware
    form_class = forms.tools_hardwareForm


class tools_hardwareCreateView(generic.CreateView):
    model = models.tools_hardware
    form_class = forms.tools_hardwareForm


class tools_hardwareDetailView(generic.DetailView):
    model = models.tools_hardware
    form_class = forms.tools_hardwareForm


class tools_hardwareUpdateView(generic.UpdateView):
    model = models.tools_hardware
    form_class = forms.tools_hardwareForm
    pk_url_kwarg = "pk"


class tools_hardwareDeleteView(generic.DeleteView):
    model = models.tools_hardware
    success_url = reverse_lazy("hoisting_rigging_app_tools_hardware_list")

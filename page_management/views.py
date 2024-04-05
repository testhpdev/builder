from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class PagesListView(generic.ListView):
    model = models.Pages
    form_class = forms.PagesForm


class PagesCreateView(generic.CreateView):
    model = models.Pages
    form_class = forms.PagesForm


class PagesDetailView(generic.DetailView):
    model = models.Pages
    form_class = forms.PagesForm
    slug_url_kwarg = "slug"


class PagesUpdateView(generic.UpdateView):
    model = models.Pages
    form_class = forms.PagesForm
    slug_url_kwarg = "slug"


class PagesDeleteView(generic.DeleteView):
    model = models.Pages
    success_url = reverse_lazy("page_management_Pages_list")

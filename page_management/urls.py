from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Pages", api.PagesViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("page_management/Pages/", views.PagesListView.as_view(), name="page_management_Pages_list"),
    path("page_management/Pages/create/", views.PagesCreateView.as_view(), name="page_management_Pages_create"),
    path("page_management/Pages/detail/<slug:slug>/", views.PagesDetailView.as_view(), name="page_management_Pages_detail"),
    path("page_management/Pages/update/<slug:slug>/", views.PagesUpdateView.as_view(), name="page_management_Pages_update"),
    path("page_management/Pages/delete/<slug:slug>/", views.PagesDeleteView.as_view(), name="page_management_Pages_delete"),

)

from django.urls import path, include
from rest_framework import routers

from . import api
from . import views
from . import htmx


router = routers.DefaultRouter()
router.register("appForm", api.appFormViewSet)
router.register("liftDescription", api.liftDescriptionViewSet)
router.register("mobileCrane", api.mobileCraneViewSet)
router.register("overheadCrane", api.overheadCraneViewSet)
router.register("tools_hardware", api.tools_hardwareViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("hoisting_rigging_app/appForm/", views.appFormListView.as_view(), name="hoisting_rigging_app_appForm_list"),
    path("hoisting_rigging_app/appForm/create/", views.appFormCreateView.as_view(), name="hoisting_rigging_app_appForm_create"),
    path("hoisting_rigging_app/appForm/detail/<int:pk>/", views.appFormDetailView.as_view(), name="hoisting_rigging_app_appForm_detail"),
    path("hoisting_rigging_app/appForm/update/<int:pk>/", views.appFormUpdateView.as_view(), name="hoisting_rigging_app_appForm_update"),
    path("hoisting_rigging_app/appForm/delete/<int:pk>/", views.appFormDeleteView.as_view(), name="hoisting_rigging_app_appForm_delete"),
    path("hoisting_rigging_app/liftDescription/", views.liftDescriptionListView.as_view(), name="hoisting_rigging_app_liftDescription_list"),
    path("hoisting_rigging_app/liftDescription/create/", views.liftDescriptionCreateView.as_view(), name="hoisting_rigging_app_liftDescription_create"),
    path("hoisting_rigging_app/liftDescription/detail/<int:pk>/", views.liftDescriptionDetailView.as_view(), name="hoisting_rigging_app_liftDescription_detail"),
    path("hoisting_rigging_app/liftDescription/update/<int:pk>/", views.liftDescriptionUpdateView.as_view(), name="hoisting_rigging_app_liftDescription_update"),
    path("hoisting_rigging_app/liftDescription/delete/<int:pk>/", views.liftDescriptionDeleteView.as_view(), name="hoisting_rigging_app_liftDescription_delete"),
    path("hoisting_rigging_app/mobileCrane/", views.mobileCraneListView.as_view(), name="hoisting_rigging_app_mobileCrane_list"),
    path("hoisting_rigging_app/mobileCrane/create/", views.mobileCraneCreateView.as_view(), name="hoisting_rigging_app_mobileCrane_create"),
    path("hoisting_rigging_app/mobileCrane/detail/<int:pk>/", views.mobileCraneDetailView.as_view(), name="hoisting_rigging_app_mobileCrane_detail"),
    path("hoisting_rigging_app/mobileCrane/update/<int:pk>/", views.mobileCraneUpdateView.as_view(), name="hoisting_rigging_app_mobileCrane_update"),
    path("hoisting_rigging_app/mobileCrane/delete/<int:pk>/", views.mobileCraneDeleteView.as_view(), name="hoisting_rigging_app_mobileCrane_delete"),
    path("hoisting_rigging_app/overheadCrane/", views.overheadCraneListView.as_view(), name="hoisting_rigging_app_overheadCrane_list"),
    path("hoisting_rigging_app/overheadCrane/create/", views.overheadCraneCreateView.as_view(), name="hoisting_rigging_app_overheadCrane_create"),
    path("hoisting_rigging_app/overheadCrane/detail/<int:pk>/", views.overheadCraneDetailView.as_view(), name="hoisting_rigging_app_overheadCrane_detail"),
    path("hoisting_rigging_app/overheadCrane/update/<int:pk>/", views.overheadCraneUpdateView.as_view(), name="hoisting_rigging_app_overheadCrane_update"),
    path("hoisting_rigging_app/overheadCrane/delete/<int:pk>/", views.overheadCraneDeleteView.as_view(), name="hoisting_rigging_app_overheadCrane_delete"),
    path("hoisting_rigging_app/tools_hardware/", views.tools_hardwareListView.as_view(), name="hoisting_rigging_app_tools_hardware_list"),
    path("hoisting_rigging_app/tools_hardware/create/", views.tools_hardwareCreateView.as_view(), name="hoisting_rigging_app_tools_hardware_create"),
    path("hoisting_rigging_app/tools_hardware/detail/<int:pk>/", views.tools_hardwareDetailView.as_view(), name="hoisting_rigging_app_tools_hardware_detail"),
    path("hoisting_rigging_app/tools_hardware/update/<int:pk>/", views.tools_hardwareUpdateView.as_view(), name="hoisting_rigging_app_tools_hardware_update"),
    path("hoisting_rigging_app/tools_hardware/delete/<int:pk>/", views.tools_hardwareDeleteView.as_view(), name="hoisting_rigging_app_tools_hardware_delete"),

    path("hoisting_rigging_app/htmx/appForm/", htmx.HTMXappFormListView.as_view(), name="hoisting_rigging_app_appForm_htmx_list"),
    path("hoisting_rigging_app/htmx/appForm/create/", htmx.HTMXappFormCreateView.as_view(), name="hoisting_rigging_app_appForm_htmx_create"),
    path("hoisting_rigging_app/htmx/appForm/delete/<int:pk>/", htmx.HTMXappFormDeleteView.as_view(), name="hoisting_rigging_app_appForm_htmx_delete"),
    path("hoisting_rigging_app/htmx/liftDescription/", htmx.HTMXliftDescriptionListView.as_view(), name="hoisting_rigging_app_liftDescription_htmx_list"),
    path("hoisting_rigging_app/htmx/liftDescription/create/", htmx.HTMXliftDescriptionCreateView.as_view(), name="hoisting_rigging_app_liftDescription_htmx_create"),
    path("hoisting_rigging_app/htmx/liftDescription/delete/<int:pk>/", htmx.HTMXliftDescriptionDeleteView.as_view(), name="hoisting_rigging_app_liftDescription_htmx_delete"),
    path("hoisting_rigging_app/htmx/mobileCrane/", htmx.HTMXmobileCraneListView.as_view(), name="hoisting_rigging_app_mobileCrane_htmx_list"),
    path("hoisting_rigging_app/htmx/mobileCrane/create/", htmx.HTMXmobileCraneCreateView.as_view(), name="hoisting_rigging_app_mobileCrane_htmx_create"),
    path("hoisting_rigging_app/htmx/mobileCrane/delete/<int:pk>/", htmx.HTMXmobileCraneDeleteView.as_view(), name="hoisting_rigging_app_mobileCrane_htmx_delete"),
    path("hoisting_rigging_app/htmx/overheadCrane/", htmx.HTMXoverheadCraneListView.as_view(), name="hoisting_rigging_app_overheadCrane_htmx_list"),
    path("hoisting_rigging_app/htmx/overheadCrane/create/", htmx.HTMXoverheadCraneCreateView.as_view(), name="hoisting_rigging_app_overheadCrane_htmx_create"),
    path("hoisting_rigging_app/htmx/overheadCrane/delete/<int:pk>/", htmx.HTMXoverheadCraneDeleteView.as_view(), name="hoisting_rigging_app_overheadCrane_htmx_delete"),
    path("hoisting_rigging_app/htmx/tools_hardware/", htmx.HTMXtools_hardwareListView.as_view(), name="hoisting_rigging_app_tools_hardware_htmx_list"),
    path("hoisting_rigging_app/htmx/tools_hardware/create/", htmx.HTMXtools_hardwareCreateView.as_view(), name="hoisting_rigging_app_tools_hardware_htmx_create"),
    path("hoisting_rigging_app/htmx/tools_hardware/delete/<int:pk>/", htmx.HTMXtools_hardwareDeleteView.as_view(), name="hoisting_rigging_app_tools_hardware_htmx_delete"),
)

from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("equipmentsList", api.equipmentsListViewSet)
router.register("liftDescriptions", api.liftDescriptionsViewSet)
router.register("mobileCrane", api.mobileCraneViewSet)
router.register("overheadCrane", api.overheadCraneViewSet)
router.register("planAttachment", api.planAttachmentViewSet)
router.register("planForm", api.planFormViewSet)
router.register("planSketch", api.planSketchViewSet)
router.register("workAssignment", api.workAssignmentViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("lift_plan_app/equipmentsList/", views.equipmentsListListView.as_view(), name="lift_plan_app_equipmentsList_list"),
    path("lift_plan_app/equipmentsList/create/", views.equipmentsListCreateView.as_view(), name="lift_plan_app_equipmentsList_create"),
    path("lift_plan_app/equipmentsList/detail/<int:pk>/", views.equipmentsListDetailView.as_view(), name="lift_plan_app_equipmentsList_detail"),
    path("lift_plan_app/equipmentsList/update/<int:pk>/", views.equipmentsListUpdateView.as_view(), name="lift_plan_app_equipmentsList_update"),
    path("lift_plan_app/equipmentsList/delete/<int:pk>/", views.equipmentsListDeleteView.as_view(), name="lift_plan_app_equipmentsList_delete"),
    path("lift_plan_app/liftDescriptions/", views.liftDescriptionsListView.as_view(), name="lift_plan_app_liftDescriptions_list"),
    path("lift_plan_app/liftDescriptions/create/", views.liftDescriptionsCreateView.as_view(), name="lift_plan_app_liftDescriptions_create"),
    path("lift_plan_app/liftDescriptions/detail/<int:pk>/", views.liftDescriptionsDetailView.as_view(), name="lift_plan_app_liftDescriptions_detail"),
    path("lift_plan_app/liftDescriptions/update/<int:pk>/", views.liftDescriptionsUpdateView.as_view(), name="lift_plan_app_liftDescriptions_update"),
    path("lift_plan_app/liftDescriptions/delete/<int:pk>/", views.liftDescriptionsDeleteView.as_view(), name="lift_plan_app_liftDescriptions_delete"),
    path("lift_plan_app/mobileCrane/", views.mobileCraneListView.as_view(), name="lift_plan_app_mobileCrane_list"),
    path("lift_plan_app/mobileCrane/create/", views.mobileCraneCreateView.as_view(), name="lift_plan_app_mobileCrane_create"),
    path("lift_plan_app/mobileCrane/detail/<int:pk>/", views.mobileCraneDetailView.as_view(), name="lift_plan_app_mobileCrane_detail"),
    path("lift_plan_app/mobileCrane/update/<int:pk>/", views.mobileCraneUpdateView.as_view(), name="lift_plan_app_mobileCrane_update"),
    path("lift_plan_app/mobileCrane/delete/<int:pk>/", views.mobileCraneDeleteView.as_view(), name="lift_plan_app_mobileCrane_delete"),
    path("lift_plan_app/overheadCrane/", views.overheadCraneListView.as_view(), name="lift_plan_app_overheadCrane_list"),
    path("lift_plan_app/overheadCrane/create/", views.overheadCraneCreateView.as_view(), name="lift_plan_app_overheadCrane_create"),
    path("lift_plan_app/overheadCrane/detail/<int:pk>/", views.overheadCraneDetailView.as_view(), name="lift_plan_app_overheadCrane_detail"),
    path("lift_plan_app/overheadCrane/update/<int:pk>/", views.overheadCraneUpdateView.as_view(), name="lift_plan_app_overheadCrane_update"),
    path("lift_plan_app/overheadCrane/delete/<int:pk>/", views.overheadCraneDeleteView.as_view(), name="lift_plan_app_overheadCrane_delete"),
    path("lift_plan_app/planAttachment/", views.planAttachmentListView.as_view(), name="lift_plan_app_planAttachment_list"),
    path("lift_plan_app/planAttachment/create/", views.planAttachmentCreateView.as_view(), name="lift_plan_app_planAttachment_create"),
    path("lift_plan_app/planAttachment/detail/<int:pk>/", views.planAttachmentDetailView.as_view(), name="lift_plan_app_planAttachment_detail"),
    path("lift_plan_app/planAttachment/update/<int:pk>/", views.planAttachmentUpdateView.as_view(), name="lift_plan_app_planAttachment_update"),
    path("lift_plan_app/planAttachment/delete/<int:pk>/", views.planAttachmentDeleteView.as_view(), name="lift_plan_app_planAttachment_delete"),
    path("lift_plan_app/planForm/", views.planFormListView.as_view(), name="lift_plan_app_planForm_list"),
    path("lift_plan_app/planForm/create/", views.planFormCreateView.as_view(), name="lift_plan_app_planForm_create"),
    path("lift_plan_app/planForm/detail/<int:pk>/", views.planFormDetailView.as_view(), name="lift_plan_app_planForm_detail"),
    path("lift_plan_app/planForm/update/<int:pk>/", views.planFormUpdateView.as_view(), name="lift_plan_app_planForm_update"),
    path("lift_plan_app/planForm/delete/<int:pk>/", views.planFormDeleteView.as_view(), name="lift_plan_app_planForm_delete"),
    path("lift_plan_app/planSketch/", views.planSketchListView.as_view(), name="lift_plan_app_planSketch_list"),
    path("lift_plan_app/planSketch/create/", views.planSketchCreateView.as_view(), name="lift_plan_app_planSketch_create"),
    path("lift_plan_app/planSketch/detail/<int:pk>/", views.planSketchDetailView.as_view(), name="lift_plan_app_planSketch_detail"),
    path("lift_plan_app/planSketch/update/<int:pk>/", views.planSketchUpdateView.as_view(), name="lift_plan_app_planSketch_update"),
    path("lift_plan_app/planSketch/delete/<int:pk>/", views.planSketchDeleteView.as_view(), name="lift_plan_app_planSketch_delete"),
    path("lift_plan_app/workAssignment/", views.workAssignmentListView.as_view(), name="lift_plan_app_workAssignment_list"),
    path("lift_plan_app/workAssignment/create/", views.workAssignmentCreateView.as_view(), name="lift_plan_app_workAssignment_create"),
    path("lift_plan_app/workAssignment/detail/<int:pk>/", views.workAssignmentDetailView.as_view(), name="lift_plan_app_workAssignment_detail"),
    path("lift_plan_app/workAssignment/update/<int:pk>/", views.workAssignmentUpdateView.as_view(), name="lift_plan_app_workAssignment_update"),
    path("lift_plan_app/workAssignment/delete/<int:pk>/", views.workAssignmentDeleteView.as_view(), name="lift_plan_app_workAssignment_delete"),

)

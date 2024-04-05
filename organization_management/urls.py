from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("User", api.UserViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("organization_management/User/", views.UserListView.as_view(), name="organization_management_User_list"),
    path("organization_management/User/create/", views.UserCreateView.as_view(), name="organization_management_User_create"),
    path("organization_management/User/detail/<int:pk>/", views.UserDetailView.as_view(), name="organization_management_User_detail"),
    path("organization_management/User/update/<int:pk>/", views.UserUpdateView.as_view(), name="organization_management_User_update"),
    path("organization_management/User/delete/<int:pk>/", views.UserDeleteView.as_view(), name="organization_management_User_delete"),

)

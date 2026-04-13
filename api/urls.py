from django.urls import path

from api.views import get_health_check, CategoryListAPIView, UserListAPIView, UserCreateAPIView, ItemListAPIView, \
    RegisterUserAPIView

# TODO: 5 for routing
urlpatterns = [
    path("health-check/", get_health_check, name="health-check"),
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("users/create/", UserCreateAPIView.as_view(), name="user-create"),

]
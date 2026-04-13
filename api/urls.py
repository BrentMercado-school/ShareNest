from django.urls import path

from api.views import (
    CategoryListAPIView,
    CurrentUserAPIView,
    ItemListAPIView,
    LoginUserAPIView,
    RegisterUserAPIView,
    UserCreateAPIView,
    UserItemsAPIView,
    UserListAPIView,
    get_health_check,
)

# TODO: 5 for routing
urlpatterns = [
    path("health-check/", get_health_check, name="health-check"),
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("users/", UserListAPIView.as_view(), name="user-list"),
    path("users/create/", UserCreateAPIView.as_view(), name="user-create"),
    path("items/", ItemListAPIView.as_view(), name="item-list"),
    path("users/register/", RegisterUserAPIView.as_view(), name="register"),
    path("users/login/", LoginUserAPIView.as_view(), name="login"),
    path("users/me/", CurrentUserAPIView.as_view(), name="login"),
    path("users/owned-items/", UserItemsAPIView.as_view(), name="user-item-list"),
]

from rest_framework import generics, status
from django.http import JsonResponse
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category, User, Item
from api.serializers import (
    CategorySerializer,
    UserSerializer,
    ItemSerializer,
    RegisterUserSerializer,
    LoginUserSerializer,
)


# TODO: 4 for controlling what data the API returns
def get_health_check(request):
    return JsonResponse({"status": "ok", "message": "API is running"}, status=200)


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ItemListAPIView(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class RegisterUserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]


class LoginUserAPIView(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = UserSerializer(serializer.validated_data["user"]).data
        request.session["user_id"] = user.get("id")

        return Response(
            {
                "user": {
                    "id": user.get("id"),
                    "name": user.get("name"),
                    "email": user.get("email"),
                },
                "message": "Login Successful",
            }
        )


class CurrentUserAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):

        userId = request.session.get("user_id")

        try:
            currentUser = User.objects.get(id=userId)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(UserSerializer(currentUser).data)

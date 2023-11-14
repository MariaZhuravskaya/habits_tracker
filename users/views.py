
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import IsOwner
# from users.permissions import IsOwner
from users.serializers import UserSerializers


class UserListView(generics.ListAPIView):
    """
    Представление для просмотра списка пользователей
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class UserCreateView(generics.CreateAPIView):
    """
    Представление для создания пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRetrieveView(generics.RetrieveAPIView):
    """
    Представление для просмотра пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class UserUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsOwner]


class UserDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [IsAuthenticated, IsOwner]



from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from atomic_habits.models import Habits
from atomic_habits.paginators import HabitsPagination
from atomic_habits.permissions import IsOwner
from atomic_habits.serializers import AtomicHabitsSerializers


class HabitsCreateView(generics.CreateAPIView):
    """
    Представление для создания привычки
    """
    queryset = Habits.objects.all()
    serializer_class = AtomicHabitsSerializers
    permission_classes = [IsAuthenticated]


class HabitsListView(generics.ListAPIView):
    """
    Представление для просмотра списка привычек
    """
    queryset = Habits.objects.all()
    serializer_class = AtomicHabitsSerializers
    pagination_class = HabitsPagination
    # permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """
        Список публичных привычек
        """
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Habits.objects.all()
        else:
            return Habits.objects.filter(is_pablish=True)


class HabitsRetrieveView(generics.RetrieveAPIView):
    """
    Представление для просмотра привычки
    """
    queryset = Habits.objects.all()
    serializer_class = AtomicHabitsSerializers
    permission_classes = [IsOwner]


class HabitsUpdateView(generics.UpdateAPIView):
    """
    Представление для изменения привычки
    """
    queryset = Habits.objects.all()
    serializer_class = AtomicHabitsSerializers
    permission_classes = [IsOwner]


class HabitsDestroyView(generics.DestroyAPIView):
    """
    Представление для удаления привычки
    """
    queryset = Habits.objects.all()
    serializer_class = AtomicHabitsSerializers
    permission_classes = [IsOwner]

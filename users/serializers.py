from rest_framework import serializers

from atomic_habits.models import Habits
from atomic_habits.serializers import AtomicHabitsSerializers
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления пользователя
    """

    habits = serializers.SerializerMethodField()

    def get_habits(self, obj_user):
        habits = Habits.objects.filter(user=obj_user)
        for habit in habits:
            return (f"place: {habit.place}, time: {habit.time}, action: {habit.action}, is_pleasant: {habit.is_pleasant}, "
                    f"related_habit: {habit.related_habit}, period: {habit.period}, reward: {habit.reward}, "
                    f"time_performance: {habit.time_performance}, is_pablish: {habit.is_pablish}")

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'city', 'habits']

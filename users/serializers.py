from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from atomic_habits.models import Habits
from users.models import User


class UserSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления пользователя
    """
    habits = serializers.SerializerMethodField()

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    def get_habits(self, obj_user):
        habits = Habits.objects.filter(user=obj_user)
        for habit in habits:
            return (f"place: {habit.place}, time: {habit.time}, action: {habit.action}, "
                    f"is_pleasant: {habit.is_pleasant}, {habit.related_habit}, period: {habit.period}, "
                    f"reward: {habit.reward}, time_performance: {habit.time_performance}, "
                    f"is_pablish: {habit.is_pablish}")

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'chat_id', 'city', 'habits']

from rest_framework import serializers

from atomic_habits.models import Habits
from atomic_habits.validators import RewardRelatedHabitValidator


class AtomicHabitsSerializers(serializers.ModelSerializer):
    """
    Сериализатор для представления привычки
    """

    class Meta:
        model = Habits
        fields = '__all__'
        validators = [RewardRelatedHabitValidator(fields=('is_pleasant', 'reward'))]

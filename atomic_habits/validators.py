from rest_framework import serializers


class RewardRelatedHabitValidator:
    """
    Исключить одновременный выбор связанной привычки и указания вознаграждения
    """
    def __init__(self, fields):
        self.fields = fields

    def __call__(self, fields, *args, **kwargs):
        if fields.get('related_habit') and fields.get('reward'):
            raise serializers.ValidationError(
                'Исключён одновременный выбор связанной привычки и указания вознаграждения.'
            )

        if fields.get('related_habit') and not fields.get('is_pleasant'):
            raise serializers.ValidationError(
                'В связанные привычки могут попадать только привычки с признаком приятной привычки.'
            )

        if fields.get('is_pleasant'):
            if fields.get('reward') or fields.get('related_habit'):
                raise serializers.ValidationError('У приятной привычки не может быть вознаграждения или связанной '
                                                  'привычки.'
                                                  )



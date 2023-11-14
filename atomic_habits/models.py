from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=100,
                              verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE,
                                      verbose_name='связанная привычка', **NULLABLE)
    period = models.IntegerField(default=1, verbose_name='периодичность',
                                 validators=[MaxValueValidator(7), MinValueValidator(1)])
    reward = models.CharField(max_length=50, verbose_name='вознаграждение', **NULLABLE)
    time_performance = models.IntegerField(default=120, verbose_name='время на выполнение',
                                           validators=[MaxValueValidator(120), MinValueValidator(0)])
    is_pablish = models.BooleanField(default=False, verbose_name='признак публичности')

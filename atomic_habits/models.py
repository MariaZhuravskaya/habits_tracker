from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Period(models.TextChoices):
    ONE = 'one'
    TWO = 'two'
    THREE = 'three'
    FOUR = 'four'
    FIVE = 'five'
    SIX = 'six'
    DAILY = 'daily'


class Habits(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='время выполнения')
    action = models.CharField(max_length=100, verbose_name='действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки') # Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='связанная привычка', **NULLABLE)  #  важно указывать для полезных привычек, но не для приятных.
    period = models.CharField(max_length=9, choices=Period.choices, default=Period.DAILY, verbose_name='периодичность')
    reward = models.CharField(max_length=50, verbose_name='вознаграждение', **NULLABLE)
    time_performance = models.IntegerField(default=120, verbose_name='время на выполнение', validators=[MaxValueValidator(120), MinValueValidator(0)])
    is_pablish = models.BooleanField(default=False, verbose_name='признак публичности')






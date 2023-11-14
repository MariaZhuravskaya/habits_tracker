from datetime import datetime
from datetime import timedelta

from atomic_habits.models import Habits


def check_time():
    """Отправка сообщения в телеграм"""
    time_now = datetime.now()
    start_time = time_now - timedelta(minutes=10)
    finish_time = time_now + timedelta(minutes=10)
    habits = Habits.objects.filter(time__gte=start_time).filter(time__lte=finish_time)

    for habit in habits:
        action = habit.action
        place = habit.place
        time = habit.time
        time_performance = habit.time_performance

        habit.time += timedelta(days=habit.period)
        habit.save()
        text = f'Напоминание о выполнении привычки  {action} в {time} в {place}'
        print(text)
        return text

        # time = datetime.now().time()
    #
    # time_start_task = datetime.now() - timedelta(minutes=1)
    #
    # data_habit = Habits.objects.filter(time__gte=time_start_task)
    #
    # for item in data_habit.filter(time__lte=time):




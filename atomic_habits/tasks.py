from celery import shared_task
import requests
from datetime import datetime
from atomic_habits.models import Habits
from config import settings


@shared_task
def chat_bot_reminders():
    TELEGRAM_BOT_API_KEY = settings.TELEGRAM_BOT_API_KEY
    TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID
    habits = Habits.objects.all()
    time_now = datetime.now().time().strftime('%H:%M')
    weekday = datetime.today().weekday()
    for habit in habits:
        action = habit.action
        place = habit.place
        time = habit.time.strftime('%H:%M')
        period = habit.period
        if time_now == time and weekday <= period:
            message = f'Напоминание о выполнении привычки  {action} в {time} в {place}'
            url = (f"https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/"
                   f"sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")
            print(requests.get(url).json())

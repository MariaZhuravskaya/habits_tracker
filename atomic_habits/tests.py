
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status

from atomic_habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self) -> None:
        """Подготовка данных перед каждым тестом"""
        self.client = APIClient()
        self.user = User.objects.create(email='adminka@gmail.com', password='1q2w3e4r')
        self.client.force_authenticate(user=self.user)
        self.user.save()
        self.habit = Habits.objects.create(
            place="бассейн",
            time="00:09:00",
            action="проплыть 1 200 метров",
            is_pleasant=False,
            period="daily",
            time_performance=120,
            is_pablish=False,
            related_habit=None,
            user=self.user
        )

    def test_create_habit(self):
        """
        тестирование создания привычки
        """
        data = {
            'place': self.habit.place,
            'time': self.habit.time,
            'action': self.habit.action,
            'is_pleasant': True,
            'period': self.habit.period,
            'time_performance': self.habit.time_performance,
            'is_pablish': True,
            'user': self.user.id,
        }
        response = self.client.post(
            '/atomic_habits/create/',
            data=data
        )
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_list_habit(self):
        """
        тестирование вывода списка привычек
        """
        response = self.client.get(
            reverse('atomic_habits:list'),
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'count': 0, 'next': None, 'previous': None, 'results': []
            }
        )

    def test_retrieve_habit(self):
        """
        тестирование вывода 1 привычки
        """
        response = self.client.get(
            '/atomic_habits/' + str(self.habit.id)
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habit(self):
        """
        тестирование изменения привычки
        """
        data = {
            'place': self.habit.place,
            'time': self.habit.time,
            'action': self.habit.action,
            'is_pleasant': True,
            'period': self.habit.period,
            'time_performance': self.habit.time_performance,
            'is_pablish': True,
            'user': self.user.id,
        }
        response = self.client.patch(
            '/atomic_habits/update/' + str(self.habit.id),
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """
        тестирование удаления привычки
        """
        response = self.client.delete(
            '/atomic_habits/delete/' + str(self.habit.id)
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def tearDown(self):
        User.objects.all().delete()
        Habits.objects.all().delete()


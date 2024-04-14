from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from users.models import User
from habits.models import Habit


class HabitTestCase(APITestCase):
    """Тест модели Habit"""

    def setUp(self) -> None:

        # Тестовый пользователь
        self.user = User.objects.create(email='testuser@test.ru')

        # Аутентификация пользователя
        self.client.force_authenticate(user=self.user)

        # Тестовая привычка
        self.habit = Habit.objects.create(
            creator=self.user,
            place='В парке',
            time="07:00:00",
            action='Слушать музыку',
            is_pleasant=True,
            frequency=1,
            time_to_complete=10,
            is_public=True
        )

    def test_create_habit(self):
        """ Тест CREATE habit """

        data = {
            'place': 'Дом',
            'time': "07:00:00",
            'action': 'Пить чай',
            'is_pleasant': False,
            'frequency': 2,
            'time_to_complete': 120
        }

        habit_create_url = reverse('habits:habit_create')
        response = self.client.post(habit_create_url, data=data)

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED,
        )

        self.assertEqual(
            response.json().get('action'),
            data.get('action')
        )

        self.assertTrue(
            Habit.objects.get(pk=self.habit.pk).action,
            data.get('action')
        )

        # Проверяем наличие записи в базе данных
        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        """ Тест READ LIST habit """

        habit_list_url = reverse('habits:habit_list')

        response = self.client.get(habit_list_url)

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Habit.objects.get(pk=self.habit.pk).action,
            response.json().get('results')[0].get('action'))

    def test_retrieve_habit(self):
        """ Тест READ ONE habit """

        habit_one_url = reverse('habits:habit_get', args=[self.habit.pk])

        response = self.client.get(habit_one_url)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )

        response = response.json()

        self.assertEqual(response.get('creator'), self.user.pk)
        self.assertEqual(response.get('place'), 'В парке')
        self.assertEqual(response.get('time'), "07:00:00")
        self.assertEqual(response.get('action'), 'Слушать музыку')

    def test_update_habit(self):
        """ Тест UPDATE habit """

        data = {
            'place': 'updated place',
            'action': 'updated action',
            'frequency': 3,
            'time_to_complete': 110
        }

        habit_update_url = reverse('habits:habit_update', args=[self.habit.pk])

        response = self.client.patch(habit_update_url, data)

        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
        )
        response = response.json()

        self.assertEqual(response.get('place'), 'updated place')
        self.assertEqual(response.get('action'), 'updated action')
        self.assertEqual(response.get('frequency'), 3)
        self.assertEqual(response.get('time_to_complete'), 110)

    def test_delete_habit(self):
        """ Тест DELETE habit """

        habit_delete_url = reverse('habits:habit_delete', args=[self.habit.pk])

        response = self.client.delete(habit_delete_url)

        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT,
        )
        self.assertFalse(
            Habit.objects.all().exists(),
        )

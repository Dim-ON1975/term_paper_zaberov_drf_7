from django.utils import timezone

from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    '''Привычка'''
    creator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cоздатель привычки', **NULLABLE)
    link_nice_habit = models.ForeignKey('self', verbose_name='Связанная привычка', on_delete=models.CASCADE, **NULLABLE,
                                        related_name='habit')

    place = models.CharField(max_length=200, verbose_name='Место привычки')
    time = models.TimeField(default=timezone.now, verbose_name='Время привычки')
    action = models.CharField(max_length=250, verbose_name='Действие привычки')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки', **NULLABLE)
    frequency = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность')
    reward = models.CharField(max_length=250, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.PositiveSmallIntegerField(default=120, verbose_name='Время на выполнение', **NULLABLE)
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я {self.action} в {self.time} {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

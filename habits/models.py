from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    owner = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='владелец')

    habit_useful = models.CharField(max_length=255, verbose_name='привычка полезная')
    is_pleasant = models.BooleanField(default=True, verbose_name='приятная/вознаграждение')
    habit_pleasant = models.CharField(**NULLABLE, max_length=255, verbose_name='привычка приятная')
    award = models.CharField(**NULLABLE, max_length=255, verbose_name='вознаграждение')

    place = models.CharField(max_length=255, verbose_name='место')
    in_time = models.TimeField(verbose_name='время')
    time_to_complete = models.PositiveIntegerField(default=120, verbose_name='время на выполнение, сек.')
    frequency = models.PositiveIntegerField(default=1, verbose_name='периодичность, дн.')

    is_public = models.BooleanField(default=False, verbose_name='публичная')

    def __str__(self):
        return self.habit_useful

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

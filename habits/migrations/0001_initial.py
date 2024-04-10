# Generated by Django 4.2.8 on 2024-04-10 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit_useful', models.CharField(max_length=255, verbose_name='привычка полезная')),
                ('is_pleasant', models.BooleanField(default=True, verbose_name='приятная/вознаграждение')),
                ('habit_pleasant', models.CharField(blank=True, max_length=255, null=True, verbose_name='привычка приятная')),
                ('award', models.CharField(blank=True, max_length=255, null=True, verbose_name='вознаграждение')),
                ('place', models.CharField(max_length=255, verbose_name='место')),
                ('in_time', models.TimeField(verbose_name='время')),
                ('time_to_complete', models.PositiveIntegerField(default=120, max_length=120, verbose_name='время на выполнение, сек.')),
                ('frequency', models.PositiveIntegerField(default=1, verbose_name='периодичность, дн.')),
                ('is_public', models.BooleanField(default=False, verbose_name='публичная')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='владелец')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]

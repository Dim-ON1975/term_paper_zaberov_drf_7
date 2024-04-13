from rest_framework import serializers

from habits.models import Habit
from habits.validators import NiceHabitValidator, RelatedHabitsPublicValidator, TimeHabitValidator, \
    FrequencyHabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'creator', 'link_nice_habit', 'place', 'time', 'action', 'is_pleasant', 'frequency',
                  'reward', 'time_to_complete', 'is_public')
        validators = [
            NiceHabitValidator(fields),
            RelatedHabitsPublicValidator(field='link_nice_habit'),
            TimeHabitValidator(field='time_to_complete'),
            FrequencyHabitValidator(field='frequency')
        ]

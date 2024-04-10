from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'owner', 'habit_useful', 'is_pleasant', 'habit_pleasant', 'award', 'place', 'in_time', 'time_to_complete',
        'frequency', 'is_public',)
    list_filter = ('owner', 'habit_useful', 'is_pleasant', 'habit_pleasant', 'award', 'place', 'frequency', 'is_public',)
    search_fields = ('habit_useful', 'habit_pleasant', 'award', 'place',)

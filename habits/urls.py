from django.urls import path
from habits.apps import HabitsConfig

from habits.views import (HabitSerializeListAPIView, HabitSerializeRetrieveAPIView, HabitSerializeCreateAPIView,
                          HabitSerializeUpdateAPIView, HabitSerializeDestroyAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/', HabitSerializeListAPIView.as_view(), name='habit_list'),
    path('habit/<int:pk>/', HabitSerializeRetrieveAPIView.as_view(), name='habit_get'),
    path('habit/create/', HabitSerializeCreateAPIView.as_view(), name='habit_create'),
    path('habit/update/<int:pk>/', HabitSerializeUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitSerializeDestroyAPIView.as_view(), name='habit_retrieve'),
]

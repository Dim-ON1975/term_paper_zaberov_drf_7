from django.db.models import Q
from rest_framework import generics

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsCreator
from habits.serializers import HabitSerializer
from rest_framework.permissions import IsAuthenticated


class HabitSerializeListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPaginator

    def get_queryset(self):
        """ Фильтрация запроса:
        привычки текущего пользователя или публичные """
        user = self.request.user
        return Habit.objects.filter(Q(creator=user) | Q(is_public=True))


class HabitSerializeRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """ Фильтрация запроса:
        привычки текущего пользователя или публичные """
        user = self.request.user
        return Habit.objects.filter(Q(creator=user) | Q(is_public=True))


class HabitSerializeCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """Привязка пользователя к создаваемой привычке"""
        new_habit = serializer.save()
        new_habit.creator = self.request.user
        new_habit.save()


class HabitSerializeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]


class HabitSerializeDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsCreator]

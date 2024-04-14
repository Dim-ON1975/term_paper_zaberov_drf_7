from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    id_telegram = models.CharField(max_length=50, verbose_name="Телеграм ID", **NULLABLE)
    avatar = models.ImageField(upload_to='users/%Y/%m/%d/', **NULLABLE, verbose_name='аватар')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

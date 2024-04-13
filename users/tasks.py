from django.utils import timezone
from celery.utils.log import get_task_logger

from core.celery import app
from users.models import User

logger = get_task_logger(__name__)


@app.task
def user_not_is_active(*args, **kwargs):
    """ Деактивация пользователя, если он не заходил на сайт более месяца """
    datetime_calculated = timezone.localtime(timezone.now()) - timezone.timedelta(days=31)
    users = User.objects.filter(last_login__lt=datetime_calculated, is_active=True)
    if users.exists():
        for user in users:
            if not user.is_superuser:
                user.is_active = False
                user.save()
                logger.info(f'Пользователь {user.email} деактивирован.')
    else:
        users_count = User.objects.all().count()
        logger.info(f'Всего зарегистрировано {users_count} пользователей(-я). '
                    f'Деактивация пользователей не требуется.')

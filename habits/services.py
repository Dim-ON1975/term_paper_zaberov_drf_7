import requests

from core.settings import TG_API_KEY


class HabitBot:
    """ Отправка сообщений в телеграм """

    URL = 'https://api.telegram.org/bot'
    TOKEN = TG_API_KEY

    def send_message(self, text: str, chat_id: str):
        """
        Отправка сообщения в телеграм.
        :object text: Текст сообщения, str.
        :object chat_id: Телеграм ID пользователя, str.
        """
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )

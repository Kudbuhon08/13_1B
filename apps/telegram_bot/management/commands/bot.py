from django.core.management.base import BaseCommand

from apps.telegram_bot.views import bot

class Command(BaseCommand):
    help = 'Bot'

    def handle(self, *args, **kwargs):
        print("Запуск бота прошла успешно")
        bot.polling(none_stop=True, interval=0)
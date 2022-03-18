import os

import django
from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)

def setup_django():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "DjangoAdminPanel.DjangoAdminPanel.settings"
    )
    os.environ.update({"DJANGO_ALLOW_ASYNC_UNSAFE": "true"})
    django.setup()

if __name__ == '__main__':
    setup_django()
    executor.start_polling(dp, on_startup=on_startup)


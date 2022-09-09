from asyncio import create_task

from aiogram import executor
from loguru import logger

from src.Handlers import *
from src.Middlewares import (
    LoggingMiddleware,
    UserMiddleware,
    SetupRoleMiddleware,
    TranslationMiddleware
)
from src.Services import ScheduleService, BinanceService
import requests as r


async def on_startup(x):
    # await settings.bot.set_webhook(settings.webhooks_data['url'])
    create_task(ScheduleService.run_schedule())


async def on_shutdown(x):
    logger.info('Bot finished')
    # await settings.bot.delete_webhook()


def setup_middlewares():
    settings.dp.middleware.setup(LoggingMiddleware())
    settings.dp.middleware.setup(UserMiddleware())
    settings.dp.middleware.setup(SetupRoleMiddleware())
    settings.dp.middleware.setup(TranslationMiddleware())


# def bind_filters():
#     settings.dp.filters_factory.bind(RolesFilter)


def start_polling():
    setup_middlewares()
    executor.start_polling(settings.dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
    logger.info('Script finished')


if __name__ == '__main__':
    start_polling()
    # executor.start_webhook(
    #     dispatcher=settings.dp,
    #     webhook_path=settings.webhooks_data['path'],
    #     on_startup=on_startup,
    #     on_shutdown=on_shutdown,
    #     skip_updates=True,
    #     host=settings.webhooks_data['host'],
    #     port=settings.webhooks_data['port'],
    # )

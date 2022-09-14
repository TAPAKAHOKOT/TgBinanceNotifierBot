from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from loguru import logger

logger.info('Loaded dotenv')


class Settings:
    def __init__(self):
        self.is_testing = getenv('TESTING_MODE') == 'TRUE'
        logger.info(f'Is testing = {self.is_testing}')

        self.token = getenv('TEST_BOT_TOKEN') if self.is_testing else getenv('BOT_TOKEN')
        self.admins = getenv('ADMINS').split(',')
        logger.info(f'Admins = {self.admins}')

        logger.info('Loaded .env variables')

        self.bot = Bot(token=self.token)
        logger.info('Created Bot')

        self.dp = Dispatcher(self.bot, storage=MemoryStorage())
        logger.info('Created Dispatcher')

        self.binance_data = {
            'max_price': -1,
            'duplicate_price': -1,
            'Aleshka_No': ['s0ceff263993230dfb14dca326e709fd0', 's91df547c6d4d39fc89645b8394a59bbd']
        }

        self.webhooks_data = {
            'path': getenv('WEBHOOK_PATH', ''),
            'url': getenv('WEBHOOK_URL'),
            'host': getenv('WEBAPP_HOST'),
            'port': getenv('WEBAPP_PORT')
        }

        self.number = 1.171

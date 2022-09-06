from aiogram import types

from Configs import translations
from Settings import settings


# <<<<<<<<<<<<<<<<<< Any message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message(message: types.Message):
    await message.answer(translations.get('answers.dont-understand'))

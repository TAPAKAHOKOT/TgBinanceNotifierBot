from aiogram import types

from Configs import translations
from Settings import settings


# <<<<<<<<<<<<<<<<<< Any message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["num"])
async def any_message(message: types.Message):
    try:
        number = settings.number
        spred_number = settings.spred_number
        await message.answer(f'Число: {number}, Курс: {spred_number}')
    except Exception as e:
        await message.answer(f'Ошибка: {e}')


# <<<<<<<<<<<<<<<<<< Any message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(regexp=r"(([0-9]*[.])?[0-9]+)")
async def any_message(message: types.Message):
    try:
        number = float(message.text)
        if number > 2:
            settings.spred_number = number
        else:
            settings.number = number
        await message.answer(f'Новое число: {settings.number}, Новый курс: {settings.spred_number}')
    except ValueError as e:
        await message.answer(f'Ошибка: {e}')


# <<<<<<<<<<<<<<<<<< Any message >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler()
async def any_message(message: types.Message):
    await message.answer(translations.get('answers.dont-understand'))

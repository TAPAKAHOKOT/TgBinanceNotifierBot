from aiogram import types

from Configs import translations
from Settings import settings
from src.Filters import IsRootFilter
from src.Keyboards import CommandsKeyboards


# <<<<<<<<<<<<<<<<<< Command [answering with keyboard] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(IsRootFilter(), commands=["start"])
async def command_start_example(message: types.Message):
    await message.answer(
        translations.get('commands.answers.start').format(
            user_name=message['from']['first_name'],
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=CommandsKeyboards.get_main_keyboard()
    )

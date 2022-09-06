from aiogram import types

from Configs import translations
from Settings import settings
from Tables import Role
from src.Filters import IsRootFilter, IsAdminFilter
from src.Keyboards import CommandsKeyboards
from src.Services import SettingsService, ExampleService


# <<<<<<<<<<<<<<<<<< Command [answering with keyboard] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(IsRootFilter(), commands=["start"])
async def command_start_example(message: types.Message, role: Role):
    await message.answer(
        translations.get('commands.answers.start').format(
            user_name=message['from']['first_name'],
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=CommandsKeyboards.get_main_keyboard(role)
    )


# <<<<<<<<<<<<<<<<<< Command [answering with keyboard] >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["start"])
async def command_start_example(message: types.Message, role: Role):
    await message.answer(
        translations.get('commands.answers.start').format(
            user_name=message['from']['first_name'],
            bot_name=(await settings.bot.get_me()).first_name
        ),
        reply_markup=CommandsKeyboards.get_main_keyboard(role)
    )


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["settings"])
async def command_help_example(message: types.Message):
    inline = SettingsService.get_settings_main_callback()
    await message.answer(translations.get('commands.answers.settings'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["help"])
async def command_help_example(message: types.Message):
    inline = ExampleService.get_example_inline_callback()
    await message.answer(translations.get('commands.answers.help'), reply_markup=inline)


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(IsRootFilter(), commands=["role"])
async def command_admin_example(message: types.Message):
    await message.answer(translations.get('commands.answers.role.root'))


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(IsAdminFilter(), commands=["role"])
async def command_admin_example(message: types.Message):
    await message.answer(translations.get('commands.answers.role.admin'))


# <<<<<<<<<<<<<<<<<< Command with callback >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(commands=["role"])
async def command_admin_example(message: types.Message):
    await message.answer(translations.get('commands.answers.role.user'))

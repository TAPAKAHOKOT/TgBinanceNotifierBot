from aiogram import types
from aiogram.dispatcher.filters import Text

from Configs import translations
from Settings import settings
from src.Filters.RolesFilter import IsRootFilter
from src.States import WriteToAllUsersForm


@settings.dp.message_handler(IsRootFilter(),
                             Text(equals=translations.get_in_all_languages('keyboards.buttons.write-to-all-users')))
async def write_to_all_users_message(message: types.Message):
    await WriteToAllUsersForm.write_to_all_users.set()
    await message.answer(translations.get('keyboards.answers.write-to-all-users'))


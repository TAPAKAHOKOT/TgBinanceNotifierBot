from aiogram import types

from Configs import translations
from Settings import settings
from Tables import UserSettings, Role
from src.Callbacks import settings_callback
from src.Keyboards import CommandsKeyboards
from src.Services import SettingsService


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=language] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(settings_callback.main_inline_data.filter(value='language'))
async def settings_callback_language(call: types.CallbackQuery, callback_data: dict):
    inline = SettingsService.get_settings_languages_callback()
    await call.message.edit_text(
        translations.get('callbacks.answers.choose-language'),
        reply_markup=inline
    )


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=language] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(settings_callback.language_inline_data.filter())
async def settings_callback_language_callback(call: types.CallbackQuery, callback_data: dict,
                                              user_settings: UserSettings, role: Role):
    user_settings = SettingsService.update_language(callback_data['value'], user_settings)

    await call.message.answer(
        translations.get('callbacks.answers.language-updated-to').format(
            language=user_settings.language if user_settings else None),
        reply_markup=CommandsKeyboards.get_main_keyboard(role)
    )

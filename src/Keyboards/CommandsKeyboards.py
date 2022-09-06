from aiogram import types

from Configs import translations
from Tables import Role


class CommandsKeyboards:
    @staticmethod
    def get_main_keyboard(role: Role) -> types.ReplyKeyboardMarkup:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start.add(
            types.KeyboardButton(text=translations.get('keyboards.buttons.hi')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.joke')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.another-keyboard')),

            types.KeyboardButton(text=''),
            types.KeyboardButton(text='/settings'),
            types.KeyboardButton(text=''),

            types.KeyboardButton(text=''),
            types.KeyboardButton(text=translations.get('keyboards.buttons.write-to-dev')),
            types.KeyboardButton(text=''),
        )

        if role.role == 'root':
            start.add(
                types.KeyboardButton(text=''),
                types.KeyboardButton(text=translations.get('keyboards.buttons.write-to-all-users')),
                types.KeyboardButton(text='')
            )

        return start

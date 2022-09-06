from aiogram import types


class CommandsKeyboards:

    @staticmethod
    def get_start_keyboard() -> types.ReplyKeyboardMarkup:
        start = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        start.add(
            types.KeyboardButton(text=''),
            types.KeyboardButton(text='/start'),
            types.KeyboardButton(text=''),
        )

        return start

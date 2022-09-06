from aiogram import types

from Configs import translations


class ExampleKeyboard:
    @staticmethod
    def get_test_keyboard() -> types.ReplyKeyboardMarkup:
        test = types.ReplyKeyboardMarkup(resize_keyboard=True)
        test.add(
            types.KeyboardButton(text='/start'),
        )
        return test

    @staticmethod
    def get_main_keyboard() -> types.ReplyKeyboardMarkup:
        main = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        main.add(
            types.KeyboardButton(text=translations.get('keyboards.buttons.hi')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.joke')),
            types.KeyboardButton(text=translations.get('keyboards.buttons.another-keyboard')),
        )

        return main

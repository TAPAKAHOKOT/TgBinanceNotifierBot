from aiogram.types.inline_keyboard import InlineKeyboardMarkup

from src.Callbacks import example_callback


class ExampleService:
    @staticmethod
    def get_example_inline_callback() -> InlineKeyboardMarkup:
        return example_callback.example_inline

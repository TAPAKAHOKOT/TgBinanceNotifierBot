from aiogram import types
from aiogram.dispatcher.filters import Text

from Configs import translations
from Settings import settings
from src.Callbacks import example_callback
from src.Keyboards import ExampleKeyboard


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=number] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_inline_data.filter(type="number"))
async def callback_number_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(
        translations.get('callbacks.answers.number-value').format(value=callback_data['value']))


# <<<<<<<<<<<<<<<<<< Callback action with [filtering by type=letter] >>>>>>>>>>>>>>>>>>
@settings.dp.callback_query_handler(example_callback.example_inline_data.filter(type="letter"))
async def callback_letter_example(call: types.CallbackQuery, callback_data: dict):
    await call.message.edit_text(
        translations.get('callbacks.answers.letter-value').format(value=callback_data['value']))


# <<<<<<<<<<<<<<<<<< Message with filters by many words >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.hi')))
async def hello_message_example(message: types.Message):
    await message.answer(translations.get('keyboards.answers.hello'))


# <<<<<<<<<<<<<<<<<< Message with filters by one word >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.joke')))
async def joke_message_example(message: types.Message):
    await message.answer(translations.get('keyboards.answers.joke'))


# <<<<<<<<<<<<<<<<<< Message with filters by one word >>>>>>>>>>>>>>>>>>
@settings.dp.message_handler(Text(equals=translations.get_in_all_languages('keyboards.buttons.another-keyboard')))
async def joke_message_example(message: types.Message):
    await message.answer(
        translations.get('keyboards.answers.another-keyboard'),
        reply_markup=ExampleKeyboard.get_test_keyboard()
    )

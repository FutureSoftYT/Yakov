from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

task = CallbackData('check','task')

KB_start_task = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔑 Start Task', callback_data='start_task')]
    ]
)

kb_getuser = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👤 GET USER INFO BY ID', callback_data='get_user')]
    ]
)


kb_changeinfo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🔵 CHANGE TWITTER', callback_data='twitter')
         ],
        [
            InlineKeyboardButton(text='🟡 INPUT TECTUM ADDRESS', callback_data='address')
        ]
    ]
)

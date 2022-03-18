from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_mainmenu = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🔑 JOIN AIRDROP')
        ],
        [
            KeyboardButton(text='👫 REFERRAL'),
            KeyboardButton(text='👤 PROFILE')
        ],
        [
            KeyboardButton(text='🎉 AIRDROP REWARDS'),
            KeyboardButton(text='💰 BALANCE')
        ]
    ]
)

kb_mainmenu_admin = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text='🔑 JOIN AIRDROP')
        ],
        [
            KeyboardButton(text='👫 REFERRAL'),
            KeyboardButton(text='👤 PROFILE')
        ],
        [
            KeyboardButton(text='🎉 AIRDROP REWARDS'),
            KeyboardButton(text='💰 BALANCE')
        ],
        [
            KeyboardButton(text='⚙️ Admin Menu')
        ]
    ]
)

kb_joiningairdrop = ReplyKeyboardMarkup(
    row_width=2,
    resize_keyboard=True,
    keyboard=[

        [
            KeyboardButton(text='🔸 CONTINUE')
        ],
        [
            KeyboardButton(text='🔙 Back To Menu')
        ]
    ]
)
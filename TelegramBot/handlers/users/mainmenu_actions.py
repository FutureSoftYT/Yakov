from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data.config import BOT_NAME
from filters import AdminFilter
from keyboards.default.kb_mainmenu import kb_joiningairdrop
from keyboards.inline.inlinesimplekb import kb_getuser, kb_changeinfo
from loader import dp
from states.get_input import GetuserInfo
from utils.db_api.db_commands import select_user, select_all_info, set_address, set_twitter


@dp.message_handler(text='🔑 JOIN AIRDROP')
async def join_drop(message: types.Message):
    await message.answer('would you like to continue?',reply_markup=kb_joiningairdrop)
    await GetuserInfo.chooseone.set()


@dp.message_handler(text='👫 REFERRAL')
async def show_refferals(message: types.Message):
    user = await select_user(message.from_user.id)
    text = f"""🗣 TECTUM REFERRAL PROGRAM

🥇 You will earn 3000 Tectum Tokens for each referral

🔗 Your referral link:
{f'https://t.me/{BOT_NAME}?start={message.from_user.id}'}

✅ Your total Refferals: {user.refferals}.
"""

    await message.answer(text=text)


@dp.message_handler(text='👤 PROFILE')
async def show_profile(message: types.Message):
    user = await select_user(message.from_user.id)
    text = f"""
💸 Your balance: {user.balance} Tectum Tokens.

🔵 Twitter: {user.twitter_name}

🔵 Address: {user.address}
"""
    await message.answer(text, reply_markup=kb_changeinfo)


@dp.callback_query_handler(text='twitter')
async def ask_twitterinput(call: types.CallbackQuery):
    await call.message.answer('Write your new twitter link:')
    await GetuserInfo.twitter.set()


@dp.message_handler(state=GetuserInfo.twitter)
async def set_twitter_link(message: types.Message, state: FSMContext):
    twitter = message.text
    await set_twitter(message.from_user.id, twitter)
    await message.answer('Your Twitter account success edited.')
    await state.finish()


@dp.callback_query_handler(text='address')
async def ask_twitterinput(call: types.CallbackQuery):
    await call.message.answer('Input tectum wallet address:')
    await GetuserInfo.address.set()


@dp.message_handler(state=GetuserInfo.address)
async def set_twitter_link(message: types.Message, state: FSMContext):
    adress = message.text
    await set_address(message.from_user.id, adress)
    await message.answer('Your address success edited')
    await state.finish()


@dp.message_handler(text='🎉 AIRDROP REWARDS')
async def show_rewards(message: types.Message):
    text = """🏆  Airdrop Rewards

🔸 100,000 Tectum Tokens(PRESALE PRICE) in the reward pool💸

🥇 Top 20 Referrers will share 💸 1000 tokens
"""

    await message.answer(text=text)


@dp.message_handler(text='💰 BALANCE')
async def show_balance(message: types.Message):
    text = '🎉 Congrats! You have Earned %s Tectum Tokens'
    balance = await select_user(message.from_user.id)
    await message.answer(text=text % balance.balance)


@dp.message_handler(AdminFilter(), text='⚙️ Admin Menu')
async def show_adminpanel(message: types.Message):
    text = """👥 Registered:%(registrated)s
🧑‍💻 Joined in airdrop:%(joined_airdrop)s

🎖Top referrers:
%(topreffs)s
"""
    topreffs = ''
    registrated, joined_airdrop, reffers = await select_all_info()
    for index, ref in enumerate(reffers):
        topreffs += f'{index + 1}. ID {ref.user_id} : {ref.refferals} \n'

    data = {
        'registrated': registrated,
        'joined_airdrop': joined_airdrop,
        'topreffs': topreffs
    }

    await message.answer(text=text % data, reply_markup=kb_getuser)


@dp.callback_query_handler(AdminFilter(), text='get_user')
async def ask_user_id(call: types.CallbackQuery):
    text = "Send user ID. Send '-' to cancel."
    await call.message.answer(text)
    await GetuserInfo.userid.set()


@dp.message_handler(state=GetuserInfo.userid, text='-')
async def raise_givinguserinfo(message: types.Message, state: FSMContext):
    await message.answer('Canceled')
    await state.finish()


@dp.message_handler(state=GetuserInfo.userid)
async def get_userid(message: types.Message, state: FSMContext):
    try:
        user_id = int(message.text)
    except:
        await message.answer('You have not entered an ID. Try again or send "-" to cancel.')
        return False

    try:
        user = await select_user(user_id)

        text = f"""ID: {user_id}
TWITTER: {user.twitter_name}
Tectum Tokens: {user.balance}
"""
        url = f'tg://user?id={user_id}'
        kb_gotouser = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='GO TO USER 👤', url=url)]
            ]
        )
        await message.answer(text, reply_markup=kb_gotouser)
        await state.finish()

    except:
        await message.answer('User not found')
        await state.finish()

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import KeyboardButton

from data.config import MAINADMINS, AWARD_PREREF
from keyboards.default.kb_mainmenu import kb_mainmenu, kb_mainmenu_admin
from keyboards.inline.inlinesimplekb import KB_start_task
from loader import dp
from states.get_input import GetuserInfo
from utils.db_api.db_commands import add_refferer, add_user, get_user
from utils.misc.createauptcha import get_cuptcha


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    text = f"""Hi {message.from_user.first_name}! I am your friendly TECTUM AIRDROP BOT.

✅ Please complete all the tasks and submit details correctly to be eligible for the airdrop

🔸 140,000 Tectum Tokens(PRESALE PRICE) in the reward pool💸

🥇 Top 40 Referrers will share 💸 40000 tokens

👫 We will randomly choose 1000 winners from the participants who complete all the tasks.

💠 Required Tasks

🔸 join telegram group <a href="https://t.me/tectumglobal">LINK</a>, announcements <a href="https://t.me/tectumdriven">LINK</a>
🔸 follow on twitter (https://twitter.com/tectumsocial) & retweet pinned post with hashtag #tectumsoftnote #fastestblockchain

🔸Follow instagram account https://www.instagram.com/tectum.io/
🔸 Create Tectum wallet account http://wallet.tectum.io/


📘 By Participating you are agreeing to the Tectum (Airdrop) Program Terms and Conditions.

Click "🔐 “JOIN AIRDROP" to proceed.

"""

    refferer = message.get_args()
    user_id = int(message.from_user.id)

    try:
        if refferer != user_id:
            await add_refferer(user_id, refferer)
            user = await get_user(int(refferer))
            user.balance += AWARD_PREREF
            user.refferals += 1
            user.save()
    except:
        pass

    await message.answer(text=text, reply_markup=KB_start_task)


@dp.callback_query_handler(text='start_task')
async def cuptcha_show(call: types.CallbackQuery, state: FSMContext):
    generated_cuptcha, res = await get_cuptcha()

    text = f"""Please solve this cuptcha:
{generated_cuptcha} = ?
"""

    await state.update_data(result=res)

    await call.message.answer(text=text)

    await GetuserInfo.answer_cuptcha.set()


@dp.message_handler(state=GetuserInfo.answer_cuptcha)
async def check_answer(message: types.Message, state: FSMContext):
    answer = int(message.text)
    data = await state.get_data()
    correct_answer = int(data.get('result'))

    if answer == correct_answer:
        markup = kb_mainmenu
        if message.from_user.id in MAINADMINS:
            markup = kb_mainmenu_admin
        try:
            await add_user(message.from_user.id, message.from_user.username, message.from_user.first_name)
        except:
            pass
        await message.answer(text='The captcha was solved correctly',reply_markup=markup)
        await state.finish()
    else:
        await message.answer(text='You have solved the captcha incorrectly.\nPlease try again:')

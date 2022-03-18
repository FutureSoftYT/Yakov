from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import CHAT_NAME, CHANNEL_NAME, BOT_NAME, MAINADMINS, LOGIN_INS, PASSWORD_INS
from keyboards.default.kb_mainmenu import kb_mainmenu, kb_mainmenu_admin, kb_joiningairdrop
from loader import dp
from states.get_input import GetuserInfo
from utils.db_api.db_commands import get_user, set_address
from utils.misc.checktasks import getsubinfo, getTotalFollowers


@dp.message_handler(state=GetuserInfo.chooseone, text='🔸 CONTINUE')
@dp.message_handler(text='🔸 CONTINUE')
async def contineairdrop(message: types.Message, state: FSMContext):
    await state.finish()
    text = f"""🔗  Join us on telegram

💠Join Tectum chat <a href="https://t.me/tectumglobal">LINK</a> and announcements <a href="https://t.me/tectumdriven">LINK</a> """
    user = await get_user(message.from_user.id)
    if user.joined_airdrop is True:
        markup = kb_mainmenu
        if message.from_user.id in MAINADMINS:
            markup = kb_mainmenu_admin
        await message.answer('You already join', reply_markup=markup)
    else:
        await message.answer(text, parse_mode='HTML')
        await GetuserInfo.check_telegram.set()


@dp.message_handler(text='🔙 Back To Menu', state='*')
async def back_tomenu(message: types.Message, state: FSMContext):
    await state.finish()
    markup = kb_mainmenu
    if message.from_user.id in MAINADMINS:
        markup = kb_mainmenu_admin
    await message.answer('Main menu', reply_markup=markup)


@dp.message_handler(state=GetuserInfo.check_telegram, text='🔸 CONTINUE')
async def contineairdrop(message: types.Message):
    text = """➡️ Follow on twitter (https://twitter.com/tectumsocial) & retweet pinned post with hashtag #tectumsoftnote #fastestblockchain and tag 3 friends
    
🔐 After completing task, Enter your twitter profile link or username Follow"""
    tg_g = await getsubinfo(message.from_user.id, CHAT_NAME)
    tg_ch = await getsubinfo(message.from_user.id, CHANNEL_NAME)

    if tg_g and tg_ch:
        await message.answer(text, reply_markup=ReplyKeyboardRemove())
        await GetuserInfo.check_twitter.set()
        user = await get_user(message.from_user.id)
        user.tg = True
        user.save()
    else:
        await message.answer('You did not completed task !!\nCheck and press 🔸 CONTINUE')


@dp.message_handler(state=GetuserInfo.check_twitter)
@dp.message_handler(state=GetuserInfo.check_twitter, text='🔸 CONTINUE')
async def check_twitter(message: types.Message):
    check_twitter = True
    user = await get_user(message.from_user.id)
    if message.text == '🔸 CONTINUE' and user.twitter_name == '':
        await message.answer('Enter your twitter profile link or username:')
        return False
    user.twitter_name = message.text
    user.save()
    if check_twitter:
        user = await get_user(message.from_user.id)
        user.twitter_tasks = True
        user.save()
        text = """➡️Follow Instagram account 
https://www.instagram.com/tectum.io/ ✅
Send me your Instagram username:
"""
        await message.answer(text)
        await GetuserInfo.check_instagram.set()
    else:
        await message.answer('You did not completed task or invalid link please resend your link')


@dp.message_handler(state=GetuserInfo.check_instagram)
async def check_instagram(message: types.Message):
    # usernameins = message.text
    # if usernameins[0] == '@':
    #     usernameins = usernameins[1:]

    # valid = await getTotalFollowers(LOGIN_INS, PASSWORD_INS)

    valid = True

    if valid:
        await message.answer('➡️ vote on coinsniper.net (LINK) ✅',reply_markup=kb_joiningairdrop)
        await GetuserInfo.check_adress.set()
        user = await get_user(message.from_user.id)
        user.instagram = True
        user.save()
    else:
        await message.answer('Please follow our instagram and send correct username :')


@dp.message_handler(state=GetuserInfo.check_adress, text='🔸 CONTINUE')
async def check_instagram(message: types.Message):
    text = """➡️ Create Tectum wallet account 
http://wallet.tectum.io/ ✅
"""
    await message.answer(text, disable_web_page_preview=True)
    await GetuserInfo.get_address_task.set()


@dp.message_handler(state=GetuserInfo.get_address_task, text='🔸 CONTINUE')
async def ask_adress(message: types.Message):
    text = """➡️ Submit address

Submit your Tectum Token address from Tectum Wallet
"""
    await message.answer(text, reply_markup=ReplyKeyboardRemove(), disable_web_page_preview=True)
    await GetuserInfo.get_address_drop.set()


@dp.message_handler(state=GetuserInfo.get_address_drop)
async def finished_task(message: types.Message, state: FSMContext):
    try:
        await set_address(message.from_user.id, message.text)
        user = await get_user(message.from_user.id)
        user.joined_airdrop = True
        user.save()
        twitter = user.twitter_name
        adress = user.address
        url = f'https://t.me/{BOT_NAME}?start={message.from_user.id}'
        text = f"""🎉🐈Congratulations! You have successfully completed airdrop tasks

        🔐 Your Provided Data:
        ▪️Twitter: {twitter}
        ▪️Wallet address: {adress}

        📢 Invite people and earn 100 Tectum Tokens per referral

        🔗 Your Referral link: {url}

        🏁AIRDROP WILL END ON 31th of March 2022
        🔸AIRDROP DISTRIBUTION WILL START AFTER 10 of April 2022

        💎PUBLIC PRE-SALE LAUNCHED <a href="https://tectum.io/tectum-token/">HERE</a>💎
        """
        valid = True
    except Exception as e:
        print(e)
        text = f'This address already exists! please try again'
        valid = False

    if valid:
        await state.finish()
        markup = kb_mainmenu
        if message.from_user.id in MAINADMINS:
            markup = kb_mainmenu_admin
        await message.answer(text, reply_markup=markup, disable_web_page_preview=True)
    else:
        await message.answer(text, disable_web_page_preview=True)

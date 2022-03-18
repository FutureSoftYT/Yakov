from aiogram import Bot

from InstagramAPI import InstagramAPI
from asgiref.sync import sync_to_async


async def getsubinfo(user_id, chat_id):
    bot = Bot.get_current()
    chat = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    return chat.is_chat_member()


@sync_to_async
def getTotalFollowers(LOGIN, PASSWORD):
    api = InstagramAPI(LOGIN, PASSWORD)
    api.login()
    user_id = api.username_id
    followers = []
    followerss = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    for follower in followers:
        followerss.append(follower['username'])
    return followerss

import os

import django
from asgiref.sync import sync_to_async

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "DjangoAdminPanel.DjangoAdminPanel.settings"
)

django.setup()

from DjangoAdminPanel.main.models import User, Referral


@sync_to_async
def select_user(user_id: int):
    user = User.objects.get(user_id=user_id)
    return user


@sync_to_async
def select_all_info():
    users = User.objects.all().count()
    joined = User.objects.filter(joined_airdrop=True).count()
    top_refers = User.objects.order_by('-refferals')
    return users,joined,top_refers[:int(25)]


@sync_to_async()
def add_user(user_id: int, username, name):
    User(user_id=user_id, username=username, name=name).save()


@sync_to_async()
def add_refferer(user_id: int, reffere_id):
    Referral(user=user_id, referrer=int(reffere_id)).save()


@sync_to_async
def get_user(user_id: int):
    user = User.objects.get(user_id=user_id)
    return user


@sync_to_async
def set_lan(user_id: int, lan):
    user = User.objects.get(user_id=user_id)
    user.language = lan
    user.save()


@sync_to_async
def set_address(user_id: int, address):
    user = User.objects.get(user_id=user_id)
    user.address = address
    user.save()


@sync_to_async
def set_twitter(user_id: int, twitter_name):
    user = User.objects.get(user_id=user_id)
    user.twitter_name = twitter_name
    user.save()

from aiogram.dispatcher.filters.state import StatesGroup, State


class GetuserInfo(StatesGroup):
    answer_cuptcha = State()
    userid = State()
    chooseone = State()
    twitter = State()
    address = State()
    check_telegram = State()
    check_twitter = State()
    check_instagram = State()
    check_adress = State()
    get_address = State()
    get_address_task = State()
    get_address_drop = State()
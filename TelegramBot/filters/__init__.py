from aiogram import Dispatcher

from loader import dp
from .adminfilter import AdminFilter


if __name__ == "filters":
    dp.filters_factory.bind(AdminFilter)

from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStatesGroup(StatesGroup):
    default = State()
    wait_gift = State()

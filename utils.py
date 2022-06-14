
from aiogram.utils.helper import Helper, HelperMode, ListItem


class MyStates(Helper):
    mode = HelperMode.snake_case

    WAITING_NAME = ListItem()
    WAITING_AGE = ListItem()
    WAITING_ANSWER = ListItem()
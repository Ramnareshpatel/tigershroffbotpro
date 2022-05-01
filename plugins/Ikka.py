#created by by @Arjun_La_Lis_A - tg
#use with proper credits

import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter


IKKA_STRINGS = (
    "CAACAgUAAxkBAAEEmSdibfi7DJDNLvKXUAg_d9IEZ9aRegAC2gEAAq4xRgU0dhWa71lVOCQE",
    "CAACAgUAAxkBAAEEmSlibfjU3joprkYupueqGLUSxzHaXwAC2wEAAq4xRgVAtfKhbk9tdyQE",
    "CAACAgUAAxkBAAEEmStibfkjdo0zQkP37_wqgyxV_cnvpAAC3QEAAq4xRgX02QI29Tg8wCQE",
    "CAACAgUAAxkBAAEEmS1ibflA2xUP3Zu3G8SyA0rAMVRo6gAC3gEAAq4xRgUtuj0TTPE1wyQE",
    "CAACAgUAAxkBAAEEmS9ibflXVF19m3y8RlhHWO4FgstOgwAC3wEAAq4xRgX1IK_9mGx1uiQE",
    "CAACAgUAAxkBAAEEmTFibflxTWxyPtZen7gIrXR_8cAC7wAC4QEAAq4xRgXqjQtXrTG3HyQE",
    "CAACAgUAAxkBAAEEmTNibfmBU6HMwvCPvdtxGajjCKo7kAAC4gEAAq4xRgVdDX9X2CkwaSQE",
    "CAACAgUAAxkBAAEEmTVibfmV07ye5YwO6laGVO-uoa3pJAAC4wEAAq4xRgVwfqoQx__41CQE",
    "CAACAgUAAxkBAAEEmTdibfmnKnnqznC5U3BmaW28Vde-sAAC5AEAAq4xRgUHn4hkqCQvUiQE",
    "CAACAgUAAxkBAAEEmTtibfnUqR1S87ev7UOUN5YyeYPqjAAC5gEAAq4xRgVspGtVeB2vMCQE",
    "CAACAgUAAxkBAAEEmT1ibfnqLCV--grreV7yH7q338bmiQAC6AEAAq4xRgVHacMRnJYtAyQE",
    "CAACAgUAAxkBAAEEmT9ibfoC0HOeixeU5ambRle_ThF4sQAC6QEAAq4xRgXdimVXd8Po2CQE",
    "CAACAgUAAxkBAAEEmUFibfoUGRHi7gPVOh6VEZf7XydFoQAC6gEAAq4xRgWU3SyU7lgt4iQE",
    "CAACAgUAAxkBAAEEmUNibfonudva5iQvQJqgT3tSSAQDcgAC6wEAAq4xRgWYd8xHrXHvSSQE",
)


@Client.on_message(
    filters.command("ikka", COMMAND_HAND_LER) &
    f_onw_fliter
)
async def ikka(_, message):
    """ /ikka strings """
    effective_string = random.choice(IKKA_STRINGS)
    if message.reply_to_message:
        await message.reply_to_message.reply_sticker(effective_string)
    else:
        await message.reply_sticker(effective_string)

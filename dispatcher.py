from telegram.ext import *
from constants import API_KEY
from responses import error, handle_message


class BotDispatcher:

    def __init__(self):
        self.updater = Updater(API_KEY, use_context=True)
        self.dp = self.updater.dispatcher

        self.dp.add_handler(MessageHandler(Filters.text, handle_message))
        self.dp.add_error_handler(error)

        self.updater.start_polling()
        self.updater.idle()

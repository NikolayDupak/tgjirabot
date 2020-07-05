from collections import Counter
from jira import JIRA
import re
from jira.client import JIRA
import json
from Issue import Issue
from time import sleep

import logging

from telegram.ext import Updater, CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    update.message.reply_text('Start')


def send_message(context):
    """Send the alarm message."""
    if context.chat_data is not None:
        chat_id = context.chat_data['chat_id']
        context.bot.send_message(chat_id, text='Beep!')


def subscribe(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id

    context.chat_data['chat_id'] = chat_id

    update.message.reply_text('Subscribe')


def unsubscribe(update, context):
    """Remove the job if the user changed their mind."""
    if 'chat_id' not in context.chat_data:
        update.message.reply_text('You didn\'t subscribe')
        return

    del context.chat_data['chat_id']

    update.message.reply_text('You unsubscribe')


def main():
    print(__name__)
    login = dict()
    file_name = "login.json"  # use login_example.json with your name/pass
    with open(file_name, "r") as read_file:
        login = json.load(read_file)

    myIssues = Issue(login["server"], login["username"], login["password"])

    while True:
        myIssues.update()
        myIssues.print()
        sleep(10)

    '''
    """Run bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(login['token'], use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", start))
    dp.add_handler(CommandHandler("on", subscribe,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("off", unsubscribe, pass_chat_data=True))

    # Start the Bot
    updater.start_polling()

    # Block until you press Ctrl-C or the process receives SIGINT, SIGTERM or
    # SIGABRT. This should be used most of the time, since start_polling() is
    # non-blocking and will stop the bot gracefully.
    updater.idle()
'''

if __name__ == '__main__':
    main()

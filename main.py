import sys
import time
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler

def callback_test():
    print "Im in"

def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='pong!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def ashell(bot, update):
    url = send_random_picture()
    bot.sendPhoto(chat_id=update.message.chat_id, photo=url)

def send_random_picture():
    index = random.randint(0,4)
    urls = ['#','http://qraaunderarm.com/content/images/underarm-slider/underarm1day.png','http://www.healcure.org/wp-content/uploads/2015/05/Underarm-Pain-Causes-Left-Right-Breast-Sharp-Shooting-Pain-under-Armpit.jpg','http://www.lifegag.com/wp-content/uploads/2015/06/maxresdefault.jpg','http://s.hswstatic.com/gif/eliminate-underarm-odor-1.jpg']
    return urls[index]

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

TOKEN = '' 

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("ping", ping))
    # dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler([Filters.text], echo))
    dp.add_handler(RegexHandler('^(ascella)$', ashell))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
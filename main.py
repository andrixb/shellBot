import sys
import time
import random
import re

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

### UTILITY METHODS ### 
def callback_test():
    print "Im in"

def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='pong!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

### SEND RANDOM PHOTO ###
def ashell(bot, update):
    url = send_random_picture()
    bot.sendPhoto(chat_id=update.message.chat_id, photo=url)

### FIND WORD IN A SENTENCE ###
def findWord(bot, update):
    # split the sentence from update in words
    words_list = update.message.text.split()
    # lunch comparision words in list and words split array
    for x in words_list:
        # if matching call send randon photo
        if re.search(r'\b(ascella|Ascella|scella|scelle|Scella|Scelle|Ascelle|ascelle|scell|Scell|ascell|Ascell)\b', x):
           ashell(bot, update) #call 

def send_random_picture():
    index = random.randint(0,4)
    print index
    urls = ['http://www.healcure.org/wp-content/uploads/2015/06/Armpit-hair-image-Girl-with-armpit-hair.jpg','http://qraaunderarm.com/content/images/underarm-slider/underarm1day.png','http://www.healcure.org/wp-content/uploads/2015/05/Underarm-Pain-Causes-Left-Right-Breast-Sharp-Shooting-Pain-under-Armpit.jpg','http://previews.123rf.com/images/ihmb/ihmb0806/ihmb080600483/3191311-Woman-applying-deodorant-on-her-underarm--Stock-Photo-armpit.jpg','http://s.hswstatic.com/gif/eliminate-underarm-odor-1.jpg']
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
    dp.add_handler(MessageHandler([Filters.text], findWord))
    # dp.add_handler(RegexHandler('^(ascella|Ascella|scella|scelle|Scella|Scelle|Ascelle|ascelle)$', ashell))

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
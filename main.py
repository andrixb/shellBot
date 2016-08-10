import sys
import time
import random
import re
import subprocess

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from gtts import gTTS

### UTILITY METHODS ### 
def callback_test():
    print "Im in"

def ping(bot, update):
    bot.sendMessage(update.message.chat_id, text='pong!')

def echo(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.text)

def testSubprocess():
    subprocess.call(['ls', '-1'])

### SEND RANDOM PHOTO ###
def sendImage(bot, update):
    url = sendRandomPicture()
    bot.sendPhoto(chat_id=update.message.chat_id, photo=url)

### FIND WORD IN A SENTENCE ###
def findWord(bot, update):
    # split the sentence from update in words
    words_list = update.message.text.split()
    # lunch comparision words in list and words split array
    for x in words_list:
        # if matching call send randon photo
        if re.search(r'\b(ascella|Ascella|scella|scelle|Scella|Scelle|Ascelle|ascelle|scell|Scell|ascell|Ascell)\b', x):
           index=random.randint(0,4)
           if (index % 2) == 0:
               sendImage(bot, update)
           else:
               sendAudio(bot, update) #call 

def sendRandomPicture():
    index = random.randint(0,4)
    print index
    urls = ['http://www.healcure.org/wp-content/uploads/2015/06/Armpit-hair-image-Girl-with-armpit-hair.jpg','http://qraaunderarm.com/content/images/underarm-slider/underarm1day.png','http://www.healcure.org/wp-content/uploads/2015/05/Underarm-Pain-Causes-Left-Right-Breast-Sharp-Shooting-Pain-under-Armpit.jpg','http://previews.123rf.com/images/ihmb/ihmb0806/ihmb080600483/3191311-Woman-applying-deodorant-on-her-underarm--Stock-Photo-armpit.jpg','http://s.hswstatic.com/gif/eliminate-underarm-odor-1.jpg']
    return urls[index]

### GENERATE AUDIO FILE ###
def createAudio(sentence):
    tts = gTTS(text=sentence, lang='it')
    tts.save('audio_sample.mp3')
    subprocess.call(['./bin/ffmpeg', '-y', '-i', 'tmp/audio_sample.mp3', 'tmp/audio_sample.ogg'])
    return True

def sendAudio(bot, update):
    #edit for raspberryPI
    index = random.randint(0,2)
    audio_sample = ['tmp/audio_sample.ogg', 'tmp/audio_sample2.ogg']
    bot.sendVoice(chat_id=update.message.chat_id, voice=open(audio_sample[index]))

def sendSample(bot, update):
    text_to_send = ["I'ch'scell' o frat'", "uua tien'e cozze sotto e' scielle"]
    index = random.randint(0,2)
    if createAudio(text_to_send[index]) == True:
        sendAudio(bot, update)
    
# def sendAction(bot, update):
#     bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)

# def sendMessage(bot, update):
#     bot.sendMessage(chat_id=update.message.chat_id, text="I'm sorry Dave I'm afraid I can't do that.")

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

TOKEN = '259365602:AAHMAVVwEy3QXEmidYDiH4-pnZ3FbQOIU2c' 

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
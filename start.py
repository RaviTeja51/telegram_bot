from telegram.ext import Updater,CommandHandler
import telegram,os
from openpyxl import load_workbook

bot = telegram.Bot(token = os.environ['token'])
updater = Updater(token = os.environ['token'])

def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="I'am a bot created by user @RaviTeja51")
    #to store the user name and chat_id in a text file

    with open("chat_id.txt","a+") as f:
        try:
            already_existing = f.readlines()
            name = update.message.from_user.first_name
            id = update.message.chat_id
            if (str(name)+ " : "+ str(id)) not in already_existing:
                f.write(str(name)+" : "+str(id))
        except:
            print("failed")









dispatcher = updater.dispatcher
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)
updater.start_polling()

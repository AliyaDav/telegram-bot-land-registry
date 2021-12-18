import telegram
from typing import Dict
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from credentials import BOT_TOKEN, APP_URL
import logging
import os

PORT = int(os.environ.get('PORT', '8443'))

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Starting Bot...')

# global bot
# bot = telegram.Bot(token=BOT_TOKEN)

''' States'''
CHOOSING, REDIRECTING = range(2)

def start(update: Update, context: CallbackContext) -> int:

    text = update.message.text.encode('utf-8').decode()
    reply_keyboard = [['Check property ownership', 'Get NFT', 'Buy/sell property']]
    logger.info(f'User texted {text}')

    # Commands menu
    # main_menu_keyboard = [[telegram.KeyboardButton('/start')],
    #                       [telegram.KeyboardButton('/help')]]
    # reply_kb_markup = telegram.ReplyKeyboardMarkup(main_menu_keyboard,
    #                                                resize_keyboard=True,
    #                                                one_time_keyboard=True)
    # bot_welcome = "Hello! This is blockchain-based land registry. What would you like to do?"
    # update.message.reply_text(bot_welcome, reply_markup = reply_kb_markup)

    bot_welcome = "Hello! This is blockchain-based land registry. What would you like to do?"
    update.message.reply_text(bot_welcome, 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))

    return CHOOSING

def force_choosing(update: Update, context: CallbackContext) -> int:
    
    reply_keyboard = [['Check property ownership', 'Get NFT', 'Buy/sell property']]
    text = update.message.text
    logger.info(f'User texted {text}')
    update.message.reply_text('Please choose one of the following options', reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))
    
    return CHOOSING
    
def go_website(update: Update, context: CallbackContext) -> int:
    
    user = update.message.from_user
    text = update.message.text
    context.user_data['choice'] = text
    logger.info("Choice of %s: %s", user.first_name, text)    
    # message = 
    update.message.reply_text(f'Perfect! In order to {text.lower()}, we need to know more about you. Please follow the link and fill out the form:', reply_markup=ReplyKeyboardRemove())
    update.message.reply_markdown('[Blockchain Registry](http://tg-landreg.herokuapp.com/)')

    return REDIRECTING

def received_information(update: Update, context: CallbackContext) -> int:
    """Store info provided by user and ask for the next category."""
    user_data = context.user_data
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    # del user_data['choice']
    update.message.reply_text(
        "Neat! Just so you know, this is what you already told me:"
        f"{facts_to_str(user_data)} You can tell me more, or change your opinion"
        " on something.")

    return CHOOSING

def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""
    facts = [f'{key} - {value}' for key, value in user_data.items()]
    return "\n".join(facts).join(['\n', '\n'])

def done(update: Update, context: CallbackContext) -> int:
    """Display the gathered info and end the conversation."""

    update.message.reply_text("Until next time!")

    return ConversationHandler.END

def handle_message(update, context):
    text = str(update.message.text).lower()
    return text

def error(update, context):
    logger.error(f'Update {update} caused error {context.error}')

def main() -> None:
    """Run the bot."""

    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOOSING: [
                MessageHandler(Filters.text(['Check property ownership', 'Get NFT', 'Buy/sell property']), go_website
                ),
                MessageHandler(Filters.text & ~Filters.text(['Check property ownership', 'Get NFT', 'Buy/sell property']), force_choosing),
            ],
            REDIRECTING: [
                MessageHandler(Filters.text, received_information,
                )
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), done)],
    )

    dispatcher.add_handler(conv_handler)

    # updater.start_webhook(listen='0.0.0.0',
    #                   port=PORT,
                    #   key='/Users/aliyadavletshina/private.key',
                    #   cert='/Users/aliyadavletshina/cert.pem',
                        # url_path=BOT_TOKEN, 
                        # webhook_url = APP_URL + BOT_TOKEN)
    updater.start_polling()
    updater.idle()

# def set_webhook():
#    s = bot.setWebhook('{APP_URL}{HOOK}'.format(URL=APP_URL, HOOK=BOT_TOKEN))
#    if s:
#        return "webhook setup ok"
#    else:
#        return "webhook setup failed"

if __name__ == '__main__':
    main()
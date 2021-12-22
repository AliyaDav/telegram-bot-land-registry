<<<<<<< HEAD
=======
import telegram
>>>>>>> main
from typing import Dict
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
<<<<<<< HEAD
from uuid import uuid4
from telegram import ReplyKeyboardMarkup, Update
import logging
import datetime
import os
import re
import dns
# from models import User, Property
from pymongo import MongoClient
from dotenv import load_dotenv
from helpers.predict_price import predict
from helpers.create_URI import create_URI
from helpers.helpers import user_info_dict, property_info_dict, facts_to_str, \
    get_owner_data, get_property_data
from helpers.functions import MintNFT, RegisterProperty, RegisterOwner
from vars import URL, REGISTRY_ADDRESS, NFT_ADDRESS, REGISTRY_ABI, NFT_ABI

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
# PORT = int(os.environ.get('PORT', '8443'))
# MONGODB_URI = os.environ.get('MONGODB_URI')
=======
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from credentials import BOT_TOKEN, APP_URL
import logging
import os
import re

PORT = int(os.environ.get('PORT', '8443'))
>>>>>>> main

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info('Starting Bot...')

''' States'''
<<<<<<< HEAD

CHOOSING_GOAL, GETTING_NAME, CHECK_NAME, GET_DOC_TYPE, GET_DOC_NUMBER, \
 GET_HOUSE_TYPE, GET_CODICE, GET_COUNTRY, GET_REGION, GET_CITY, GET_STREET, GET_BUILDING_NUMBER,\
 GET_CAP, GET_HOUSE_TYPE, GET_FLOORS, GET_SIZE, REQUEST_ROOMS, REQUEST_SURFACE, \
     REQUEST_FLOORS, ESTIMATE_PRICE, CLOSING, REQUEST_WALLET_ADDRESS, CHOOSE_ACTION, \
         NFT_DONE, GOT_WALLET, OWNER_REGISTERED, CHECKED_PROPERTY_INFO = range(27) 

'''Bot functions'''
=======
CHOOSING_GOAL, GETTING_NAME, CHECK_NAME, GET_DOC_TYPE, GET_DOC_NUMBER, \
 GET_HOUSE_TYPE, GET_CODICE, GET_COUNTRY, GET_REGION, GET_CITY, GET_STREET, GET_BUILDING_NUMBER,\
 GET_CAP, GET_HOUSE_TYPE, GET_FLOORS, GET_SIZE, CLOSING = range(17) 
>>>>>>> main

def start(update: Update, context: CallbackContext) -> int:

    text = update.message.text.encode('utf-8').decode()
<<<<<<< HEAD

    reply_keyboard = [['Estimate house price', 'Register owner']]
    # 'Issue NFT', 'Buy/sell property'], 
    #                     ['Collateralize property', 'Check ownership once'],
    #                     ['Subscribe to ownership check']]

=======
    reply_keyboard = [['Check property ownership', 'Get NFT', 'Buy/sell property']]
>>>>>>> main
    logger.info(f'User texted {text}')

    bot_welcome = "Hello! This is blockchain-based land registry. What would you like to do?"
    if (text.lower() == 'start again')|(text.lower() == 'cancel'):
        update.message.reply_text("Let's start again. What would you like to do?", 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))
    else:
        update.message.reply_text(bot_welcome, 
                                reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                one_time_keyboard=True))
    return CHOOSING_GOAL

def force_choosing_goal(update: Update, context: CallbackContext) -> int:
    
<<<<<<< HEAD
    reply_keyboard = ['Estimate house price', 'Register owner']
    # [['Estimate house price', 'Issue NFT', 'Buy/sell property'], 
    #                     ['Collateralize property', 'Check ownership once'],
    #                     ['Subscribe to ownership check']]
    text = update.message.text
    logger.info(f'User texted {text}, user_data: {context.user_data.items()}')
=======
    reply_keyboard = [['Check property ownership', 'Get NFT', 'Buy/sell property']]
    text = update.message.text
    logger.info(f'User texted {text}')
>>>>>>> main
    update.message.reply_text('Please choose one of the following options', reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))
    
    return CHOOSING_GOAL

def get_name_surname(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
<<<<<<< HEAD
    if text not in ['Estimate house price', 'Register owner']:
        # update.message.reply_text('Please type your name and surname again')
        return CHOOSING_GOAL
=======
    if text not in ['Check property ownership', 'Get NFT', 'Buy/sell property']:
        update.message.reply_text('Please type your name and surname again')
>>>>>>> main
    else:
        context.user_data['chosen action'] = text
        update.message.reply_text(f'Perfect! In order to {text.lower()}, we need to know more about you. Please type your name and surname.')

    return GETTING_NAME

def check_name(update: Update, context: CallbackContext) -> int:

    text = update.message.text
    if len(text.split()) == 2:
        logger.info(f'User texted {text}')
        context.user_data['First name'] = text.split(' ')[0]
        context.user_data['Last name'] = text.split(' ')[1]
        update.message.reply_text(f"Your first name is {text.split(' ')[0]} and your last name is {text.split(' ')[1]}, is that correct?")
        return CHECK_NAME
    else:
        update.message.reply_text('Please provide correct name and surname')
        logger.info(f'User texted {text}, length is {len(text.split())}')
        return GETTING_NAME

def get_doc_type(update: Update, context: CallbackContext) -> int:
    
    reply_keyboard = [['Passport', 'ID card']]
    text = update.message.text
    logger.info(f'User texted {update.message.text}')
    if text not in ['Yes', 'yes', 'No', 'no']:
        context.user_data['First name'] = text.split(' ')[0]
        context.user_data['Last name'] = text.split(' ')[1]
    update.message.reply_text('Perfect! What document are you providing?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))

    return GET_DOC_TYPE

def force_choosing_doc_type(update: Update, context: CallbackContext) -> int:
    
    reply_keyboard = [['Passport', 'ID card']]
    text = update.message.text
    logger.info(f'User texted {text}')
    update.message.reply_text('Please choose one of the following options:', 
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))
    
    return GET_DOC_TYPE

def get_doc_number(update: Update, context: CallbackContext) -> int:

    text = update.message.text
    context.user_data['Doc type'] = text
    logger.info(f"User's document type is {text}")
    update.message.reply_text('Please type your document number.')

    return GET_DOC_NUMBER

def get_codice(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid document number')
        return GET_DOC_NUMBER
    else:
        context.user_data['Doc number'] = text
        logger.info(f"User's document number is {text}")
        update.message.reply_text('Now please type your fiscal code.')

        return GET_CODICE

def get_country(update: Update, context: CallbackContext) -> int:
    
    text = str(update.message.text).strip()
<<<<<<< HEAD
    logger.info(f"User typed {text}")
    if text == 'Start again':
        update.message.reply_text("Let's start again")
    else:
        update.message.reply_text("Thank you! Now we need to know more about your property. Let's start with the address. What is the country?")

    return GET_COUNTRY
=======
    if re.findall('[^a-zA-Z0-9]+', text):
        update.message.reply_text('Please provide a valid fiscal code.')
    else:
        context.user_data['Fiscal code'] = text
        logger.info(f"User's codice fiscale is {text}")
        update.message.reply_text("Perfect! We have all the necessary information to include you in the blockchain registry.\n" 
                                "Now we need to know more about yout property. Let's start with the address. What is the country?")

        return GET_COUNTRY
>>>>>>> main

def get_region(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^A-Za-z\s]+', text):
        update.message.reply_text('Please provide a valid country name.')
        return GET_COUNTRY
    else:
        context.user_data['Country'] = text
        logger.info(f"User's country is {text}")
        update.message.reply_text('What is the region?')
        return GET_REGION

def get_city(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^A-Za-z\s]+', text):
        update.message.reply_text('Please provide a valid region name.')
        return GET_REGION
    else:
        context.user_data['Region'] = text
        logger.info(f"User's region is {text}")
        update.message.reply_text('What is the city?')
        return GET_CITY

<<<<<<< HEAD
=======

>>>>>>> main
def get_street(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^A-Za-z\s]+', text):
        update.message.reply_text('Please provide a valid city name')
        return GET_CITY
    else:
        context.user_data['City'] = text
        logger.info(f"User's city is {text}")
        update.message.reply_text('What is the street?')

        return GET_STREET

<<<<<<< HEAD
=======

>>>>>>> main
def get_building_number(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^A-Za-z\s]+', text):
        update.message.reply_text('Please provide a valid street name')
        return GET_STREET
    else:
        context.user_data['Street'] = text
        logger.info(f"User's street is {text}")
        update.message.reply_text('What is the building number?')
        return GET_BUILDING_NUMBER

def get_cap(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid building number')
        return GET_BUILDING_NUMBER
    else:
        context.user_data['Building number'] = text
        logger.info(f"User's building number is {text}")
        update.message.reply_text('What is the zip code?')

        return GET_CAP

def get_house_type(update: Update, context: CallbackContext) -> int:
    
    reply_keyboard = [['Single family detached house', 'Apartment'], 
                        ['Castle', 'Chalet', 'Bungalow', 'Cave house']]
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid zip code.')
        return GET_CAP
    else:
        context.user_data['Cap'] = text
        logger.info(f"User's cap os {text}")
        update.message.reply_text('What is the type of the property?', reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                one_time_keyboard=True))

        return GET_HOUSE_TYPE

def get_floors(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if text not in ['Single family detached house', 'Apartment','Castle', 'Chalet', 'Bungalow', 'Cave house']:
        update.message.reply_text('Please choose one of the following options')
        return GET_HOUSE_TYPE
    else:
        context.user_data['Property type'] = text
        logger.info(f"User's house type is {text}")
        update.message.reply_text('How many floors does the property have?')

        return GET_FLOORS

def get_size(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide valid number')
        return GET_FLOORS
    else:
        context.user_data['Floors'] = text
        logger.info(f"User's property has {text} floors")
        update.message.reply_text('What is the size of the property in sq meters?')

        return GET_SIZE

<<<<<<< HEAD
=======
# def go_website(update: Update, context: CallbackContext) -> int:
    
#     user = update.message.from_user
#     text = update.message.text
#     context.user_data['choice'] = text
#     logger.info("Choice of %s: %s", user.first_name, text)
#     logger.info(context.user_data)
#     update.message.reply_text(f'Perfect! In order to {text.lower()}, we need to know more about you. Please follow the link and fill out the form:', reply_markup=ReplyKeyboardRemove())
#     update.message.reply_markdown('[Blockchain Registry](https://webpage-landreg.herokuapp.com/)')

#     return REDIRECTING

>>>>>>> main
def received_information(update: Update, context: CallbackContext) -> int:
    """Display the gathered info and ask to check."""
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid property size')
        return GET_SIZE
    else:
        context.user_data['Property size'] = text
<<<<<<< HEAD
        context.user_data['id'] = str(uuid4())
=======
>>>>>>> main
        reply_keyboard = [['All correct', 'Start again']]
        update.message.reply_text(
            "Awesome! Thank you, now we are all set. Please check the correctness of your data:"
            f"{facts_to_str(context.user_data)}", reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                                one_time_keyboard=True))

<<<<<<< HEAD
        return CHECKED_PROPERTY_INFO

# add ownership check menu, + functions of the contracts that the user has access to.

def request_wallet_address(update: Update, context: CallbackContext) -> int:
    
    text = str(update.message.text).strip()
    if re.findall('[^a-zA-Z0-9]+', text):
        update.message.reply_text('Please provide a valid fiscal code.')
        return GET_DOC_NUMBER
    else:
        context.user_data['Fiscal code'] = text
        logger.info(f"User's fiscal code is {text}")
        update.message.reply_text('Please provide your wallet address')

        return REQUEST_WALLET_ADDRESS

def store_wallet_address(update: Update, context: CallbackContext) -> int:

    text = update.message.text
    logger.info(f"User wallet address - {text}")
    context.user_data['wallet address'] = text

    reply_keyboard = [['All correct', 'Start again']]
    update.message.reply_text(
        "Awesome! Thank you, now we are all set. Please check the correctness of your data:"
        f"{facts_to_str(context.user_data)}", reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))
    # context.user_data['id'] = str(uuid4())

    return GOT_WALLET

def register_property(update: Update, context: CallbackContext) -> int:

    property_data = get_property_data(context)
    RegisterProperty(URL, REGISTRY_ADDRESS, REGISTRY_ABI, **property_data)

    reply_keyboard = [['Estimate house price', 'Issue NFT', 'Buy/sell property'], 
                        ['Collateralize property', 'Check ownership once'],
                        ['Subscribe to ownership check']]

    update.message.reply_text("Your property has been registered. What would you like to do?",
                            reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True,
                            one_time_keyboard=True))
    
    return CHOOSE_ACTION

def register_owner(update: Update, context: CallbackContext) -> int:

    owner_data = get_owner_data(context)
    RegisterOwner(URL, REGISTRY_ADDRESS, REGISTRY_ABI, **owner_data)
    update.message.reply_text(
        "Awesome! You are successfully registered. In order to register a property, please deposit money to the address: {REGISTRY_ADDRESS}",
        'Please type "done" when payment is completed.')

    return OWNER_REGISTERED

def require_payment(update: Update, context: CallbackContext) -> int:

    text = update.message.text 
    logger.info(f"User typed {text}")   
    update.message.reply_text(f'In order to proceed please deposit money to the address: {REGISTRY_ADDRESS}')

    return OWNER_REGISTERED

def mint_nft(update: Update, context: CallbackContext) -> int:

    property_data = {v for k, v in context.user_data.items() if k in \
        ['Country', 'Region', 'City', 'Street', 'buildnig number', 'Cap', 'Property type', 
        'Floors', 'Property size']}

    token_uri = create_URI(**property_data)

    MintNFT(URL, NFT_ADDRESS, NFT_ABI, token_uri)
    logger.info(f"Token uri is {token_uri}")
    update.message.reply_text(f'Your NFT is successfully issued. Your token URI is {token_uri}',
                                'Type /start to go to the beginning.')

    return NFT_DONE

def request_house_surface(update: Update, context: CallbackContext) -> int:
    
    update.message.reply_text('How much is the surface of the property?')

    return REQUEST_SURFACE

def request_house_floors(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid surface size')
        return REQUEST_SURFACE
    else:
        logger.info(f"House surface is {text}")
        context.user_data['Surface'] = text
        update.message.reply_text('Which floor is it?')

        return REQUEST_FLOORS

def request_house_rooms(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid floor')
        return REQUEST_FLOORS

    else:
        context.user_data['Floor'] = text
        update.message.reply_text('How many rooms are there?')
        return REQUEST_ROOMS

def estimate_price(update: Update, context: CallbackContext) -> int:
    
    text = update.message.text
    if re.findall('[^0-9]+', text):
        update.message.reply_text('Please provide a valid number')

        return REQUEST_ROOMS

    else:
        context.user_data['Rooms'] = text
        surface, rooms, floor = context.user_data['Surface'], context.user_data['Rooms'] ,context.user_data['Floor']
        estimation = predict(surface, rooms, floor)
        logger.info(f'Estimated price is {estimation}')
        update.message.reply_text(f"The estimated price of the house is {estimation}. Please type '/start' to go to the beginning")

        return ESTIMATE_PRICE

def close_conv(update: Update, context: CallbackContext) -> int:
    
    # storing data in MongoDB
    # client = MongoClient(MONGODB_URI)
    # db = client.landreg
    # user = user_info_dict(context.user_data)
    # user['property'] = property_info_dict(context.user_data)
    # user['date_modified'] = datetime.datetime.utcnow
    # result = db.users.insert_one(user)
    # logger.info(f'Inserted a user into db {result.inserted_id}')
    update.message.reply_text("Thank you! Our team will check all the information provided and will come back to you soon.")

    return CHOOSING_GOAL
=======
        return CLOSING

def close_conv(update: Update, context: CallbackContext) -> int:

    text = str(update.message.text).lower()
    if text == 'all correct':
        update.message.reply_text("Thank you! Our team will check all the information provided and will come back to you soon.")
        return ConversationHandler.END
    elif text == 'start again':
        return CHOOSING_GOAL

def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""

    user_facts = [f'{key}: {value}' for key, value in user_data.items() if key in \
        ['First name', 'Last name', 'Doc type', 'Doc number', 'Fiscal code']]
    property_facts = [f'{key}: {value}' for key, value in user_data.items() if key in \
        ['Country', 'Region', 'City', 'Street', 'buildnig number', 'Cap', 'Property type', 
        'Floors', 'Property size']]

    return "\n".join(user_facts + property_facts).join(['\n', '\n'])

def start_again(update: Update, context: CallbackContext) -> int:

    return CHOOSING_GOAL

def handle_message(update, context):
    text = str(update.message.text).lower()
    return text

def error(update, context):
    logger.error(f'Update {update} caused error {context.error}')
>>>>>>> main

def main() -> None:
    """Run the bot."""

    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Add conversation handler with the states CHOOSING, TYPING_CHOICE and TYPING_REPLY
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), MessageHandler(Filters.text('cancel'), start)],
        states={
            CHOOSING_GOAL: [
<<<<<<< HEAD
                MessageHandler(Filters.text('Estimate house price'), request_house_surface),
                MessageHandler(Filters.text(['Register owner']), get_name_surname
                ),
                MessageHandler(Filters.text & ~Filters.text(['Register owner', 'Estimate house price']), force_choosing_goal)
            ],
            REQUEST_SURFACE: [
                MessageHandler(Filters.text, request_house_floors)
            ],
            REQUEST_FLOORS: [
                MessageHandler(Filters.text, request_house_rooms)
            ],
            REQUEST_ROOMS: [
                MessageHandler(Filters.text, estimate_price)
            ],
            ESTIMATE_PRICE: [
                MessageHandler(Filters.text, start)
            ], 
            REQUEST_WALLET_ADDRESS: [
                MessageHandler(Filters.text, store_wallet_address)
            ],
            GOT_WALLET: [
                MessageHandler(Filters.text(['All correct']), register_owner),
                MessageHandler(~Filters.text(['All correct']), start),
            ],
            OWNER_REGISTERED: [
                MessageHandler(Filters.text(['done', 'Done']), get_country),
                MessageHandler(~Filters.text(['done', 'Done']), require_payment)
            ],
=======
                MessageHandler(Filters.text(['Check property ownership', 'Get NFT', 'Buy/sell property']), get_name_surname
                ),
                MessageHandler(Filters.text & ~Filters.text(['Check property ownership', 'Get NFT', 'Buy/sell property']), force_choosing_goal),
            ],
            # REDIRECTING: [
            #     MessageHandler(Filters.text, received_information,
            #     )],
>>>>>>> main
            GETTING_NAME: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), check_name),
                MessageHandler(Filters.text(['back', 'Back']), get_name_surname)
            ],
            CHECK_NAME: [
                MessageHandler(Filters.text(['yes', 'Yes']), get_doc_type),
                MessageHandler(Filters.text(['no', 'No']), get_name_surname),
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back', 'yes', 'Yes', 'no', 'No']), get_name_surname),
                MessageHandler(Filters.text(['back', 'Back']), get_name_surname)
            ],
            GET_DOC_TYPE: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']),get_doc_number),
                MessageHandler(Filters.text(['back', 'Back']), get_doc_type)
            ],
            GET_DOC_NUMBER: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']),get_codice), 
                MessageHandler(Filters.text(['back', 'Back']), get_doc_number)
            ],
            GET_CODICE: [
<<<<<<< HEAD
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), request_wallet_address),
=======
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_country),
>>>>>>> main
                MessageHandler(Filters.text(['back', 'Back']), get_codice)
            ],
            GET_COUNTRY: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_region),
                MessageHandler(Filters.text(['back', 'Back']), get_country)
            ],
            GET_REGION: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_city),
                MessageHandler(Filters.text(['back', 'Back']), get_region)
            ],
            GET_CITY: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_street),
                MessageHandler(Filters.text(['back', 'Back']), get_city)
            ],
            GET_STREET: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_building_number),
                MessageHandler(Filters.text(['back', 'Back']),get_street)
            ],
            GET_BUILDING_NUMBER: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_cap),
                MessageHandler(Filters.text(['back', 'Back']), get_building_number)
            ],
            GET_CAP: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_house_type),
                MessageHandler(Filters.text(['back', 'Back']), get_cap)
            ],
            GET_HOUSE_TYPE: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_floors),
                MessageHandler(Filters.text(['back', 'Back']), get_house_type)
            ],  
            GET_FLOORS: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), get_size),
                MessageHandler(Filters.text(['back', 'Back']), get_floors)
            ],                          
            GET_SIZE: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), received_information),
                MessageHandler(Filters.text(['back', 'Back']), get_size)
            ],
<<<<<<< HEAD
            CHECKED_PROPERTY_INFO: [
                MessageHandler(Filters.text('All correct'), register_property),
                MessageHandler(Filters.text('Start again'), get_country)
            ],
            CHOOSE_ACTION: [
                MessageHandler(Filters.text('Issue NFT'), mint_nft)
                # MessageHandler(Filters.text('Issue NFT'), mint_nft)
                # MessageHandler(Filters.text('Issue NFT'), mint_nft)
                # MessageHandler(Filters.text('Issue NFT'), mint_nft)
                # MessageHandler(Filters.text('Issue NFT'), mint_nft)
            ],
            NFT_DONE: [
                MessageHandler(Filters.text, close_conv)
            ],
=======
>>>>>>> main
            CLOSING: [
                MessageHandler(Filters.text & ~Filters.text(['back', 'Back']), close_conv),
                MessageHandler(Filters.text(['back', 'Back']), received_information)
            ]
        },
<<<<<<< HEAD
        fallbacks = [MessageHandler(Filters.text(['cancel', '/start']), start)]
=======
        fallbacks = [MessageHandler(Filters.text(['cancel', 'Start again', '/start']), start_again)]
>>>>>>> main
    )

    dispatcher.add_handler(conv_handler)

    # updater.start_webhook(listen='0.0.0.0',
    #                         port=PORT,
    #                 #   key='/Users/aliyadavletshina/private.key',
    #                 #   cert='/Users/aliyadavletshina/cert.pem',
    #                     url_path=BOT_TOKEN, 
    #                     webhook_url = APP_URL + BOT_TOKEN)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
<<<<<<< HEAD

=======
>>>>>>> main


from typing import Dict


def facts_to_str(user_data: Dict[str, str]) -> str:
    """Helper function for formatting the gathered user info."""

    user_facts = [f'{key}: {value}' for key, value in user_data.items() if key in \
        ['First name', 'Last name', 'Doc type', 'Doc number', 'Fiscal code', 'wallet address']]
    property_facts = [f'{key}: {value}' for key, value in user_data.items() if key in \
        ['Country', 'Region', 'City', 'Street', 'Buildnig number', 'Cap', 'Property type', 
        'Floors', 'Property size']]

    return "\n".join(user_facts + property_facts).join(['\n', '\n'])

def user_info_dict(user_data: Dict[str, str]) -> str:
    user_facts = {key:value for key, value in user_data.items() if key in \
        ['id', 'First name', 'Last name', 'Doc type', 'Doc number', 'Fiscal code']}
    
    return user_facts

def property_info_dict(user_data: Dict[str, str]) -> str:
    property_facts = [{key: value for key, value in user_data.items() if key in \
        ['id', 'Country', 'Region', 'City', 'Street', 'Buildnig number', 'Cap', 'Property type', 
        'Floors', 'Property size']}]

    return property_facts   

def handle_message(update, context):
    text = str(update.message.text).lower()
    return text

def get_owner_data(context):
    
    firstName = context.user_data['First name']
    lastName = context.user_data['Last name']
    owner_address = context.user_data['wallet address']
    codiceFiscale = context.user_data['Fiscal code'] 
    docType = context.user_data['Doc type'] 
    docNumber = context.user_data['Doc number'] 

    return (firstName, lastName, owner_address, codiceFiscale, docType, docNumber)

def get_property_data(context):
    Owner_address = context.user_data['wallet address'] 
    areaSqm = context.user_data['Property size'] 
    floor = context.user_data['Floors'] 
    zipCode = context.user_data['Cap'] 
    country = context.user_data['Country'] 
    region = context.user_data['Region'] 
    city = context.user_data['City'] 
    street = context.user_data['Street']  
    streetNumber = context.user_data['Building number']  
    addressAdditional = 'No additional info'
    houseType = context.user_data['Property type']

    return (Owner_address, int(areaSqm), int(floor), int(zipCode), country, region, city, street, streetNumber, addressAdditional, houseType)


"""Translation functions using IBM Watson."""

import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(f'{apikey}')
language_translator = LanguageTranslatorV3(
    version=f'{VERSION}',
    authenticator=authenticator
)

language_translator.set_service_url(f'{url}')

def english_french(english:str):
    """Translate english text to french."""

    if english:
        translation = language_translator.translate(
        text=english,
        model_id='en-fr').get_result()["translations"][0]["translation"]
    else:
        translation = None
    return translation

def french_english(french:str):
    """Translate french text to english."""

    if french:
        translation = language_translator.translate(
        text=french,
        model_id='fr-en').get_result()["translations"][0]["translation"]
    else:
        translation = None
    return translation

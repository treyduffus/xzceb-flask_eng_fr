"""
English to French Translator using IBM Watson
"""
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('IS3ZmVkP6cFLv1WaEruUgh0fcZqAddamV_KQasIvit7M')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)


language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com'
)




def english_to_french(english_text):
    """
    Translates english to french
    """
    if not english_text:
        return ""
    french_text = language_translator.translate(
    text=english_text,
    source="english",
    target="french").get_result()

    return french_text['translations'][0]['translation']  

def french_to_english(french_text):
    """
    Translates french to english
    """
    if not french_text:
        return ""
    english_text = language_translator.translate(
    text=french_text,
    source="french",
    target="english").get_result()
    return english_text['translations'][0]['translation'] 

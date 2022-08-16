'''language translation'''
import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()
apikey=os.environ['apikey']
url=os.environ['url']


'''translator instance'''
authenticator1=IAMAuthenticator(apikey)
translator=LanguageTranslatorV3(version='2022-08-16',authenticator=authenticator1)
translator.set_service_url(url)


def english_to_french(english_text):
    """ English to French"""
    translation = json.dumps(translator.translate(text = english_text,\
         model_id = 'en-fr').get_result(),indent=2,ensure_ascii=False)
    french_text = json.loads(translation)
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """French to English"""
    translation = json.dumps(translator.translate(text = french_text,\
         model_id = 'fr-en').get_result(),indent=2,ensure_ascii=False)
    english_text = json.loads(translation)
    return english_text['translations'][0]['translation']

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com')


def englishToFrench(english_text):
    """
    translate english to french
    """
    if english_text!='':
        french_text = str(language_translator.translate(
            text=english_text,
            model_id='en-fr'
        ).get_result()["translations"])
    else:
        return ''
    return french_text[18:-3]




def frenchToEnglish(french_text):
    """
    translate french to english
    """
    if french_text!='':
        english_text = str(language_translator.translate(
            text=french_text,
            model_id="fr-en"
        ).get_result()["translations"])
    else:return ''
    return english_text[18:-3]

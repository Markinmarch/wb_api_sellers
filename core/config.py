import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = '.env')

WB_API_TOKEN = os.getenv('WB_API_TOKEN', '')

PATH = {
    'auth': '/api/v1/offers/author',
}

URL = 'devapi-digital.wildberries.ru'
import aiohttp, asyncio

# from core.config import WB_API_TOKEN, URL, PATH

import dotenv
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path = '.env')

WB_API_TOKEN = os.getenv('WB_API_TOKEN', '')

PATH = {
    'auth': '/api/v1/offers/author',
}

URL = 'devapi-digital.wildberries.ru'


class Session:
    
    def __init__(self) -> None:
        self.wb_api_token: str = WB_API_TOKEN
        self.url: str = URL
        self.path: str = PATH['auth']
        self.headers: dict = {'Content-Type': 'applycation/json'}
        self.auth: str = 'Bearer' + ' ' + self.wb_api_token
        
    async def login(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = self.url + self.path,
                headers = self.headers
            ) as respond:
                return respond.headers
            

            
            
login = Session().login()
asyncio.run(login)
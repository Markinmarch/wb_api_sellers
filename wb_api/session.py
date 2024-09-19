import aiohttp, asyncio

from core.config import WB_API_TOKEN, URL, PATH


class Session:
    
    def __init__(self) -> None:
        self.wb_api_token: str = WB_API_TOKEN
        self.url: str = URL
        self.path: str = PATH['auth']
        self.auth: str = 'Bearer' + ' ' + self.wb_api_token
        self.headers: dict = {'Content-Type': 'applycation/json', 'Authorization': self.auth}

        
    async def login(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url = 'https://devapi-digital.wildberries.ru/api/v1/offers/author',
                headers = self.headers,
                params = {'Authorization': self.auth},
                json = {
                    'Authorization': self.auth
                }
            ) as respond:
                return respond.headers.get()
            

            
            
login = Session().login()

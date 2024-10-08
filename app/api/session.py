import aiohttp, asyncio

from ..core.config import WB_API_TOKEN, URL_OPENAPI, URL_DIGITAL, PATH


class Session:
    
    def __init__(self) -> None:
        self.wb_api_token: str = WB_API_TOKEN
        self.url: str = URL_DIGITAL
        self.path: str = PATH['auth']
        self.auth: str = 'Bearer' + ' ' + self.wb_api_token
        self.headers: dict = {'Content-Type': 'applycation/json', 'Authorization': self.auth}

        
    async def login(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                url = self.url + self.path,
                headers = self.headers,
            ) as respond:
                return respond.status
                        
login = Session().login()

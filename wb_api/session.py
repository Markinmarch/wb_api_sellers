import aiohttp

from core.config import WB_API_TOKEN, URL, PATH


class Session:
    
    def __init__(self) -> None:
        self.wb_api_token: str = WB_API_TOKEN
        self.url: str = URL
        self.path = PATH['auth']
        self.headers: dict = {'Content-Type': 'applycation/json'}
        self.auth: str = 'Bearer' + self.wb_api_token
        
    async def login(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = self.url + self.path,
                headers = self.headers
            ) as respond:
                return respond.headers
            

            
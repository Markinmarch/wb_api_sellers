if __name__ == '__main__':

    def get_start():
        import asyncio
        from main_app.wb_api.session import login
        x = asyncio.run(login)
        print(x)
        
get_start()
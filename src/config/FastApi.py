from fastapi import FastAPI

class ServiceFast:
    _api = None
    _headers_context_data = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
        "content-type": "application/json;charset=UTF-8",
        "accept-encoding": "gzip, deflate, br",
        "accept": "application/json, text/plain, */*",
    }

    def __init__(self):
        self._api = None

    def __new__(cls):
        
        cls._api = FastAPI(
            title="Datalab - Softexpert",
            version="1.0",
            description="This application to analysis the text with cloud aws bedrock",
            summary="Application generate for the group GRC [Datalab] - Softexpert ",
            swagger_ui_parameter={"syntaxHighlight.theme": "obsidian"},
            swagger_ui_init_oauth=True,
        )

        return cls._api

    def close_connection(self):
        self._api = None
from fastapi import APIRouter, Response, Form
from pydantic import BaseModel
from src.config import Debugger

class IRequest(BaseModel):
    temp: int
    humid: int
    rain: int

class Routers(Debugger):
    def __init__(self) -> None:
        super().__init__(True)
        self.routes = APIRouter(prefix='', tags=['Arduino'])
    
    def configure_routes(self):            
        @self.routes.get('/esp', name='Salvar dados')
        async def analysisFile(body):
            try:
                self.log(body)
                pass
            except Exception as __error:
                self.writeError(__error)
                raise Response(__error, status_code=500)

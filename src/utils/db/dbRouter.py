
from src.config.Debug import Debugger


class UtilsDB(Debugger):
    
    def __init__(self) -> None:
        super().__init__(True)
        

    def getAttr(self, Instance):
        try:
            instance = Instance()
            
            if not (instance.routes):
                return False
            
            instance.configure_routes()
            
            return instance.routes

        except Exception as __error:
            self.writeError(__error)
        
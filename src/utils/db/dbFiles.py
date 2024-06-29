import base64
from fastapi import  UploadFile

from src.config.Debug import Debugger


class UtilsFile(Debugger):

    __file = None

    def __init__(self) -> None:
        self.__file: str = None
        self.setDebug(True)
        
    async def readerFile(self, _imageFile: UploadFile):
        try:            
            
            fileContent = _imageFile.filename

            if not fileContent:
                self.writeError(1, p_description="Sem dados no arquivo em formato de imagem")
                
            with open(_imageFile, 'rb') as image:
                binary_data = image.read()
                
                base64_file = base64.b64decode(binary_data)
                base64_string = base64_file.decode('utf-8')
                
                self.__file = base64_string
                      
        except Exception as error:
            self.writeError(1, p_description=error, step="Leitura do arquivo")

    def getData(self):
        return self.__file
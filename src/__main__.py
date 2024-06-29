import os
import sys

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware 

from src.config import ServiceFast
from src.routes.aws import Routers
from src.utils.db import UtilsDB

load_dotenv()

app = ServiceFast()
utils = UtilsDB()

# Configure routes

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
    allow_credentials=False
)

app.include_router(utils.getAttr(Routers))

sys.path.append(os.path.abspath('./src'))
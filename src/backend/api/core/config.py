from dotenv import load_dotenv
from pathlib import Path
import os

dir_path=(Path(__file__) /".." / ".."/"..").resolve()
env_path=os.path.join(dir_path,'.env')
load_dotenv(dotenv_path=env_path)

class Settings():

    APP_TITLE:str= os.getenv("APP_TITLE")
    APP_VERSION:str=os.getenv("APP_VERSION")
    APP_HOST:str=os.getenv("APP_HOST")
    APP_PORT:int=os.getenv("APP_PORT")

settings=Settings()
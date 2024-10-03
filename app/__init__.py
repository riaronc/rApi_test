import dotenv

dotenv.load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.app_settings import app_settings
from app.api.views import search_router

from setup import initial_setup

initial_setup()


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=search_router, prefix=app_settings.api_search_prefix)
from app.error_handler import *

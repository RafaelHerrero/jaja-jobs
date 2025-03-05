import os
import logging
from datetime import timedelta


class Config:
    APP_NAME = "fin-app"
    DESCRIPTION = "FIN App"
    ENV = os.getenv("ENV", "dev")
    LOG_LEVEL = os.getenv("LOGLEVEL", logging.INFO)
    DEBUG = os.getenv("DEBUG", False)
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:42069")
    API_KEY = os.getenv("API_KEY", "1234")


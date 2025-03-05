from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from contextlib import asynccontextmanager
import requests
from src.config import Config
from pytz import utc

counter = 1

def job_counter():
    config = Config()
    print('calling recurring transaction endpoint')
    requests.get(f'{config.BACKEND_URL}/recurring-transaction/create-recurring-transactions', headers={'X-API-KEY': config.API_KEY})
    print('recurring transaction endpoint called')
    return

@asynccontextmanager
async def lifespan(_: FastAPI):
    print('app started....')
    scheduler = BackgroundScheduler(timezone=utc)
    scheduler.add_job(id="job1", func=job_counter, trigger='cron', hour='8', minute='0')
    scheduler.start()
    yield
    print('app stopped...')
    scheduler.shutdown(wait=False)

app = FastAPI(lifespan=lifespan)
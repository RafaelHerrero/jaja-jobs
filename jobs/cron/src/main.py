import requests
from src.config import Config
import time


def cron_job():
    config = Config()
    counter = 0
    while counter < 2:
        print('calling recurring transaction endpoint')
        requests.get(f'{config.BACKEND_URL}/recurring-transaction/create-recurring-transactions', headers={'X-API-KEY': config.API_KEY})
        print('recurring transaction endpoint called')
        counter += 1
        time.sleep(20)
    return

if __name__ == '__main__':
    cron_job()
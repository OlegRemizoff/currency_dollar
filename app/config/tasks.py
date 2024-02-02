from celery import shared_task
import requests
from datetime import datetime

# DB
# from django_celery_results.models import TaskResult  # тут храняться задачи
# TaskResults.object.last() - <TaskResult: <Task: 8dce6167-b520-421a-a769-b992b0fe3c32 (SUCCESS)>>
# TaskResults.object.last()__dict__ = {'task_name': None, 'status': 'SUCCESS', 'result': "hello from config.tasks"} etc



# @shared_task(name='greeting_task')
# def greeting():
#     return "Hello!"


# greeting.apply_async(countdown=10) отложить запуск


# GET USD
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
    "Content-Type": "application/json;"}

url = 'https://api.coingate.com/v2/rates/merchant/USD/RUB'


@shared_task
def get_currency() -> dict:
    response = requests.get(url, headers)
    now = datetime.utcnow().strftime('%H:%M:%S')
    id_counter = 1

    try:
        if response.status_code == 200:
            data = {
                "time": now,
                "USD": "1",
                "RUB": response.text,
            }
            return data
        else:
            return {}
    except Exception as e:
        pass



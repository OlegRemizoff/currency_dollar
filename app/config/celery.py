import os
import time

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# celery -A config worker -l info
# celery -A config flower

app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Явное указание пути для автодисковери задач
app.autodiscover_tasks([
    'config',
    # 'myapp2',
])

app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.broker_connection_retry_on_startup = True


@app.task()
def debug_task():
    time.sleep(5)
    print("Hello from debug task")



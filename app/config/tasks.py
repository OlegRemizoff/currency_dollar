from celery import shared_task

# DB
# from django_celery_results.models import TaskResult  # тут храняться задачи
# TaskResults.object.last() - <TaskResult: <Task: 8dce6167-b520-421a-a769-b992b0fe3c32 (SUCCESS)>>
# TaskResults.object.last()__dict__ = {'task_name': None, 'status': 'SUCCESS', 'result': "hello from config.tasks"} etc



@shared_task(name='greeting_task')
def greeting():
    return "Hello!"


# greeting.apply_async(countdown=10) отложить запуск
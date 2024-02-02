from django.http.response import  JsonResponse
from django_celery_results.models import TaskResult
from .tasks import get_currency



headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
    "Content-Type": "application/json;"}
url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_current_usd(request):
    data = list()
    get_currency.apply_async(countdown=10)
    all_tasks_quantity = TaskResult.objects.all() # счетчик всех запросов
    all_tasks = TaskResult.objects.all().order_by('-id')[:10]
    for task in all_tasks:
        data.append(task.result) # [{"time": "08:26:02", "USD": "1", "RUB": "90.42"}, ]
    return JsonResponse(
        {"all_quantity": str(len(all_tasks_quantity)), "data": data})







    # if not request.session.get('storage'):
    #     request.session["storage"] = list() # список, где будут храниться наши словари
    # res = get_currency()
    # request.session['storage'].append(res)
    # request.session['storage'] = request.session['storage'][-10:]  # Ограничиваем список только последними 10 значениями
    # data = request.session['storage']
    # return JsonResponse({"data": data})







# def get_current_usd(request):
#     # data = debug_task.delay()
#     # print(data)
#     return JsonResponse({"message": "Django"})







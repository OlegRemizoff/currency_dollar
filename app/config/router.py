from django.http.response import  JsonResponse
from .utils import get_currency


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
    "Content-Type": "application/json;"}
url = 'https://www.cbr-xml-daily.ru/daily_json.js'


def get_current_usd(request):
    if not request.session.get('storage'):
        request.session["storage"] = list() # список, где будут храниться наши словари
    res = get_currency()
    request.session['storage'].append(res)
    request.session['storage'] = request.session['storage'][-10:]  # Ограничиваем список только последними 10 значениями
    data = request.session['storage']
    return JsonResponse({"data": data})











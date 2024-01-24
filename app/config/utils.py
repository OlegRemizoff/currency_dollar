import requests
import time


headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", 
    "Content-Type": "application/json;"}

url = 'https://www.cbr-xml-daily.ru/daily_json.js'



def get_currency() -> dict:
    my_dict = dict()

    time.sleep(2)
    response = requests.get(url, headers)
    try:
        if response.status_code == 200:
            time_date = response.json().get("Date")
            data = response.json().get("Valute").get("USD")

            my_dict["Date"] = time_date
            my_dict["Nominal"] = data.get('Nominal')
            my_dict["Name"] = "Доллар США"
            my_dict["RUB"] = data.get('Value')
            my_dict["Previous"] =  data.get('Previous')
            return my_dict
        else:
            return {}
    except Exception as e:
        pass



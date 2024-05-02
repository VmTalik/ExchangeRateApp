import requests
from .models import ExchangeRate
from django.db import IntegrityError


def fetch_exchange_rate():
    response = None
    try:
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    except requests.ConnectionError as err:
        print('Ошибка подключения', err)
    except requests.Timeout as err:
        print('Ошибка таймаута', err)
    except requests.RequestException as err:
        print('Ошибка запроса', err)

    date = response.json()['Timestamp'].split('T')[0]
    valutes = response.json()['Valute']
    try:
        for valute in valutes:
            ExchangeRate.objects.create(charcode=valute, date=date, rate=valutes[valute]["Value"])
    except IntegrityError as err:
        print('Ошибка заполнения БД.', err)

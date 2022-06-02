import requests
import json
from datetime import datetime
from decimal import Decimal


def currency_rates(valute_code):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    valutes = json.loads(response.content)

    valute_code = valute_code.upper()
    if valute_code in valutes['Valute']:
        valute_result = Decimal(valutes['Valute'][valute_code]['Value']).quantize(Decimal('1.0000'))

        date_str = response.headers['Date']
        date_result = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')

        return valute_result, date_result

    return None
    
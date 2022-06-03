import requests
import json
from decimal import Decimal


def currency_rates(valute_code):
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    valutes = json.loads(response.content)

    valute_code = valute_code.upper()
    if valute_code in valutes['Valute']:
        return Decimal(valutes['Valute'][valute_code]['Value']).quantize(Decimal('1.0000'))

    return None


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('EUR'))

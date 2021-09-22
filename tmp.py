import requests
from currency.utils import to_decimal
from currency import choices
from currency import consts


def _get_currencies(url):
    response = requests.get(url)
    # response.raise_for_status()
    currencies = response.json()
    return currencies


def parse_fixer():
    # bank = Bank.objects.get(code_name=consts.CODE_NAME_FIXER)
    response = requests.get('http://data.fixer.io/api/latest?access_key=49ffa3b39f4f6056bc1c38783589ffe1')
    response.raise_for_status()
    currencies = response.json()
    base_type = currencies['base']
    rate_list = currencies['rates']

    available_currency_types = {
        'UAH': choices.RATE_TYPE_UAH,
    }

    # clear_cache = False

    for type, value in rate_list.items():
        currency_type = type
        if currency_type in available_currency_types:
            buy = to_decimal(value)
            sale = to_decimal(value)
            print(currency_type)
    print(base_type)
    print(buy, sale)

parse_fixer()

# from bs4 import BeautifulSoup
#
# url = 'http://vkurse.dp.ua/'
#
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
#
# dollar_currency = soup.find("div", {"id": "dollar-section"})

from unittest.mock import MagicMock

from currency import consts
from currency.tasks import parse_privatbank
from currency.models import Rate, Bank


def test_parse_privatbank(mocker):
    json_mock = lambda: [
        {"ccy": "USD", "base_ccy": "UAH", "buy": "26.55000", "sale": "26.95000"},
        {"ccy": "EUR", "base_ccy": "UAH", "buy": "31.60000", "sale": "32.20000"},
        {"ccy": "RUR", "base_ccy": "UAH", "buy": "0.35500", "sale": "0.38500"},
        {"ccy": "BTC", "base_ccy": "USD", "buy": "39316.6209", "sale": "43455.2125"},
    ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))

    # TODO
    code_name = consts.CODE_NAME_PRIVATBANK
    privatbank_data = {
        'name': 'PrivatBank',
        'url': 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        'original_url': 'https://privatbank.ua/ru',
    }
    Bank.objects.create(code_name=code_name, **privatbank_data)

    initial_count = Rate.objects.count()
    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2

    parse_privatbank()
    assert Rate.objects.count() == initial_count + 2

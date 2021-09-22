from celery import shared_task
from django.core.cache import cache
from django.core.mail import send_mail
from currency.utils import to_decimal
from currency import choices
from currency import consts
import requests
from currency.models import Rate, Bank

def _get_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task
def parse_privatbank():
    bank = Bank.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)
    currencies = _get_currencies(consts.PRIVATBANK_API_URL)

    available_currency_types = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    # clear_cache = False

    for curr in currencies:
        currency_type = curr['ccy']
        if currency_type in available_currency_types:
            currency_type = available_currency_types[curr['ccy']]

            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(
                bank=bank, type=currency_type
            ).order_by("created").last()

            # Check if new rate should be create
            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                print(f'New rate was creates: {sale} {buy}')
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
                # clear_cache = True
            else:
                print(f'Rate already exists: {sale} {buy}')

    # if clear_cache:
    #     cache.delete(consts.CACHE_KEY_LATEST_RATES)

@shared_task
def parse_monobank():
    bank = Bank.objects.get(code_name=consts.CODE_NAME_MONOBANK)
    currencies = _get_currencies(consts.MONOBANK_API_URL)

    available_currency_types = {
        840: choices.RATE_TYPE_USD,
        978: choices.RATE_TYPE_EUR,
    }

    for curr in currencies:
        currency_type = curr['currencyCodeA']
        if currency_type in available_currency_types:
            currency_type = available_currency_types[curr['currencyCodeA']]

            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            previous_rate = Rate.objects.filter(
                bank=bank, type=currency_type
            ).order_by("created").last()

            # Check if new rate should be create
            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                print(f'New rate was creates: {sale} {buy}')
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')

@shared_task
def parse_nbu():
    bank = Bank.objects.get(code_name=consts.CODE_NAME_NBU)
    currencies = _get_currencies(consts.NBU_API_URL)

    available_currency_types = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    for curr in currencies:
        currency_type = curr['cc']
        if currency_type in available_currency_types:
            currency_type = available_currency_types[curr['cc']]

            buy = to_decimal(curr['rate'])
            sale = to_decimal(curr['rate'])

            previous_rate = Rate.objects.filter(
                bank=bank, type=currency_type
            ).order_by("created").last()

            # Check if new rate should be create
            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                print(f'New rate was creates: {sale} {buy}')
                Rate.objects.create(
                    type=currency_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
            else:
                print(f'Rate already exists: {sale} {buy}')

@shared_task
def parse_fixer():
    bank = Bank.objects.get(code_name=consts.CODE_NAME_FIXER)
    currencies = _get_currencies(consts.FIXER_API_URL)
    base_type = choices.RATE_TYPE_EUR
    rate_list = currencies['rates']

    available_currency_types = {
        'UAH': choices.RATE_TYPE_UAH,
    }

    # clear_cache = False

    for rate, value in rate_list.items():
        currency_type = rate
        if currency_type in available_currency_types:
            buy = to_decimal(value)
            sale = to_decimal(value)

            previous_rate = Rate.objects.filter(
                bank=bank, type=base_type
            ).order_by("created").last()

            # Check if new rate should be create
            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                print(f'New rate was creates: {sale} {buy}')
                Rate.objects.create(
                    type=base_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
                # clear_cache = True
            else:
                print(f'Rate already exists: {sale} {buy}')

@shared_task
def parse_exchange():
    bank = Bank.objects.get(code_name=consts.CODE_NAME_EXCHANGE)
    currencies = _get_currencies(consts.EXCHANGE_API_URL)
    base_type = choices.RATE_TYPE_EUR
    rate_list = currencies['rates']

    available_currency_types = {
        'UAH': choices.RATE_TYPE_UAH,
    }

    # clear_cache = False

    for rate, value in rate_list.items():
        currency_type = rate
        if currency_type in available_currency_types:
            buy = to_decimal(value)
            sale = to_decimal(value)

            previous_rate = Rate.objects.filter(
                bank=bank, type=base_type
            ).order_by("created").last()

            # Check if new rate should be create
            if (
                    previous_rate is None or
                    previous_rate.sale != sale or
                    previous_rate.buy != buy
            ):
                print(f'New rate was creates: {sale} {buy}')
                Rate.objects.create(
                    type=base_type,
                    sale=sale,
                    buy=buy,
                    bank=bank,
                )
                # clear_cache = True
            else:
                print(f'Rate already exists: {sale} {buy}')

    # if clear_cache:
    #     cache.delete(consts.CACHE_KEY_LATEST_RATES)
@shared_task
def print_hello_world():
    print('Hello, World!')


@shared_task(
    autoretry=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 60,
    }
)
def send_email_in_background(body):
    send_mail(
        'Contact Us from Client',
        body,
        'zvemrme@gmail.com',
        ['pasha.shalimoff169@gmail.com'],
        fail_silently=False,
    )

from django.apps import AppConfig
from django.db import connection


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        from currency.models import Bank
        from currency import consts

        all_tables = connection.introspection.table_names()

        # check if table exists
        # table could be absent before initial migration
        # if Bank._meta.db_table in all_tables:
        if 'currency_bank' in all_tables:
            print('Update Banks Initial Data')
            code_name_privat = consts.CODE_NAME_PRIVATBANK
            privatbank_data = {
                'name': 'PrivatBank',
                'url': 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
                'original_url': 'https://privatbank.ua/ru',
            }
            code_name_mono = consts.CODE_NAME_MONOBANK
            monobank_data = {
                'name': 'Monobank',
                'url': 'https://api.monobank.ua/bank/currency',
                'original_url': 'https://www.monobank.ua/',
            }
            code_name_nbu = consts.CODE_NAME_NBU
            nbu_data = {
                'name': 'NBU',
                'url': 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json',
                'original_url': 'https://bank.gov.ua/',
            }
            code_name_fixer = consts.CODE_NAME_FIXER
            fixer_data = {
                'name': 'Fixer',
                'url': 'http://data.fixer.io/api/latest?access_key=49ffa3b39f4f6056bc1c38783589ffe1',
                'original_url': 'https://fixer.io/',
            }
            code_name_exchange = consts.CODE_NAME_EXCHANGE
            exchange_data = {
                'name': 'Exchange',
                'url': 'http://api.exchangeratesapi.io/v1/latest?access_key=a269aea102907112a2072c7bb6c9ea3b&format=1',
                'original_url': 'https://exchangeratesapi.io/',
            }
            Bank.objects.update_or_create(code_name=code_name_privat, defaults=privatbank_data)
            Bank.objects.update_or_create(code_name=code_name_mono, defaults=monobank_data)
            Bank.objects.update_or_create(code_name=code_name_nbu, defaults=nbu_data)
            Bank.objects.update_or_create(code_name=code_name_fixer, defaults=fixer_data)
            Bank.objects.update_or_create(code_name=code_name_exchange, defaults=exchange_data)





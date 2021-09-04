RATE_TYPE_USD = 840
RATE_TYPE_EUR = 978

RATE_TYPE_CHOICES = (
    (RATE_TYPE_USD, 'Dollar'),
    (RATE_TYPE_EUR, 'Euro'),

)

PRIVATBANK_API_URL = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
MONOBANK_API_URL = 'https://api.monobank.ua/bank/currency'

SOURCE_URLS_CHOICES = (
    PRIVATBANK_API_URL,
    MONOBANK_API_URL,
)


REQUEST_METHOD_GET = 0
REQUEST_METHOD_POST = 1

REQUEST_METHOD_CHOICES = (
    (REQUEST_METHOD_GET, 'GET'),
    (REQUEST_METHOD_POST, 'POST'),

)

REQUEST_METHOD_CHOICES_MAPPER = {value[1]: value[0] for value in REQUEST_METHOD_CHOICES}
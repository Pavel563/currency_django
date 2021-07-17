import string

from django.core.management.base import BaseCommand
from currency.models import Rate, ContactUs, Bank
import random
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Generate random records'

    def handle(self, *args, **options):
        for index in range(100):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                source=random.choice(['privatbank', 'monobank', 'vkurse']),
            )

        for index in range(100):
            ContactUs.objects.create(
                email_from=str(fake.name()) + '@gmail.com',
                subject=fake.text(),
                message=fake.text(),
            )

        for index in range(3):
            Bank.objects.create(
                name=random.choice(['privatbank', 'monobank', 'vkurse']),
                url=''.join(random.choice(string.ascii_lowercase) for _ in range(15)) + '.com',
            )

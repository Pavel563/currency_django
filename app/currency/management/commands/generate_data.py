from django.core.management.base import BaseCommand
from currency.models import Rate, ContactUs
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Generate random records'

    def handle(self, *args, **options):
        fake = Faker()
        for index in range(100):
            Rate.objects.create(
                type=random.choice(('usd', 'eur')),
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                resource=random.choice(('privatbank', 'monobank', 'vkurse')),
            )
            ContactUs.objects.create(
                email_from=str(fake.name()) + '@gmail.com',
                subject=fake.text(),
                message=fake.message(),
            )

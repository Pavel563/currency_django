# Generated by Django 3.2.5 on 2021-08-22 14:51

from django.db import migrations, models

def forwards(apps, schema_editor):
    Rate = apps.get_model('currency', 'Rate')
    Bank = apps.get_model('currency', 'Bank')

    privatbank = Bank.objects.create(
        name='PrivatBank',
        url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        original_url='https://www.privat24.ua/',
    )
    for rate in Rate.objects.all():
        if 'privatbank' in rate.source.lower():
            rate.bank = privatbank

        rate.save()


def backwards(apps, schema_editor):
    # Post = apps.get_model('blog', 'Post')
    print('HELLO FROM BACKWARDS!')


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_rate_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='original_url',
            field=models.URLField(default=None),
            preserve_default=False,
        ),
    ]
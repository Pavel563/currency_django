# Generated by Django 3.2.5 on 2021-08-24 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_alter_bank_code_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='source',
        ),
    ]

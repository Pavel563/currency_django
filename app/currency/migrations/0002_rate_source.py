# Generated by Django 3.2.4 on 2021-06-24 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='source',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]

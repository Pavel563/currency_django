# Generated by Django 3.2.4 on 2021-07-04 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_remove_contactus_email_from'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('url', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='contactus',
            name='email_from',
            field=models.CharField(default=2, max_length=64),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-04 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_watchlist_watching'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='watching',
        ),
    ]

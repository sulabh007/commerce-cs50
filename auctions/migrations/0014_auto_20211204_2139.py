# Generated by Django 3.2.8 on 2021-12-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_remove_watchlist_watching'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='title',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='title',
            field=models.ManyToManyField(related_name='watchlist', to='auctions.Listing'),
        ),
    ]

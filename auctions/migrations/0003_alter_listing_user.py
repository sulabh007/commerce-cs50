# Generated by Django 3.2.8 on 2021-12-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_categories_category_comment_listing_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_alter_listing_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]

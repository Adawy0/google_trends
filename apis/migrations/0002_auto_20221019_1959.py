# Generated by Django 3.2.16 on 2022-10-19 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalinterestdataframe',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='interestbyregion',
            options={'managed': False},
        ),
    ]
# Generated by Django 2.0.7 on 2018-08-11 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0011_auto_20180811_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='odds',
        )
    ]
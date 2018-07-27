# Generated by Django 2.0.7 on 2018-07-27 19:51

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0008_auto_20180717_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='match_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='created_at',
            field=models.DateTimeField(default=timezone.now),
        )
    ]

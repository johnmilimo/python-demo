# Generated by Django 2.0.7 on 2018-07-16 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_auto_20180714_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='match_files/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
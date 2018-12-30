# Generated by Django 2.1 on 2018-12-28 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20181228_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='time',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='date',
            field=models.DateTimeField(auto_now=True, db_index=True),
        ),
    ]

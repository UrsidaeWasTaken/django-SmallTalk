# Generated by Django 2.1 on 2018-12-05 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('chat', '0002_auto_20181205_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.ChatRoom'),
        ),
    ]

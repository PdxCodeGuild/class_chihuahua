# Generated by Django 4.1.3 on 2022-11-22 00:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_lists', '0002_todo_item_title_alter_todo_item_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo_item',
            name='date_started',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
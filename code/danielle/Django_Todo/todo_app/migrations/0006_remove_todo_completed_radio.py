# Generated by Django 4.1.3 on 2022-11-26 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_rename_completed_date_todo_completed_radio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed_radio',
        ),
    ]

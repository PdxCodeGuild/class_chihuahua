# Generated by Django 4.1.3 on 2022-11-19 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0002_remove_todo_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completion',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
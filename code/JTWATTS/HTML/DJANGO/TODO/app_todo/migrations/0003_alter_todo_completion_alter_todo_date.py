# Generated by Django 4.1.3 on 2022-11-15 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_todo', '0002_alter_todo_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completion',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
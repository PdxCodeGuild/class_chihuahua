# Generated by Django 4.1.3 on 2022-11-10 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0003_alter_todoitem_completed_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TodoItem',
            new_name='TodoItems',
        ),
    ]

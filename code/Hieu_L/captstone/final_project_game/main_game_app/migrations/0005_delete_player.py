# Generated by Django 4.1.4 on 2023-01-16 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_game_app', '0004_item_remove_player_attack_items_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='player',
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('many_app', '0002_alter_player_team_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team_name',
            field=models.ManyToManyField(blank=True, null=True, to='many_app.team'),
        ),
    ]

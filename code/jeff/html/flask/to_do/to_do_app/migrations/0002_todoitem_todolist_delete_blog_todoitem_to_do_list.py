# Generated by Django 4.1.3 on 2022-11-02 03:09

from django.db import migrations, models
import django.db.models.deletion
import to_do_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateTimeField(default=to_do_app.models.one_week_hence)),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
        migrations.AddField(
            model_name='todoitem',
            name='to_do_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='to_do_app.to_do_list'),
        ),
    ]

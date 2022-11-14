# Generated by Django 3.1.4 on 2020-12-31 18:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book_app', '0013_auto_20201231_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('yes', 'Book is out'), ('no', 'Book is in')], max_length=200)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('book', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='book_app.book')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
# Generated by Django 2.2.5 on 2019-09-16 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='Added',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 16, 5, 50, 0, 359118)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

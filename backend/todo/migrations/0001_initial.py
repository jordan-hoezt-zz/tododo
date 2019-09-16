# Generated by Django 2.2.5 on 2019-09-16 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('descripton', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

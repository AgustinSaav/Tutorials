# Generated by Django 4.2.3 on 2023-07-18 21:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_tutorial_tittle_tutorial_tutorial_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 18, 45, 36, 52478), verbose_name='date published'),
        ),
    ]

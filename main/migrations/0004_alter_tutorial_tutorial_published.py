# Generated by Django 4.2.3 on 2023-07-18 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 19, 51, 57, 982254), verbose_name='date published'),
        ),
    ]

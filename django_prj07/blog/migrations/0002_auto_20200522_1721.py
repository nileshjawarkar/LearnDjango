# Generated by Django 3.0.3 on 2020-05-22 11:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 5, 22, 11, 51, 42, 525432, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateField(verbose_name=datetime.datetime(2020, 5, 22, 11, 51, 42, 525432, tzinfo=utc)),
        ),
    ]

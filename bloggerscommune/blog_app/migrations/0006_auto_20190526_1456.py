# Generated by Django 2.1.7 on 2019-05-26 14:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0005_auto_20190522_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 14, 56, 45, 48406, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='commentonpost',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 26, 14, 56, 45, 48818, tzinfo=utc)),
        ),
    ]

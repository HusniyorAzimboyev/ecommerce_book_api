# Generated by Django 5.1.4 on 2025-01-09 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms_auth', '0002_customuser_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 9, 12, 29, 34, 464924, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-24 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(default=datetime.date(2023, 9, 24)),
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-24 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_booking_booking_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_one',
            new_name='booked_on',
        ),
    ]

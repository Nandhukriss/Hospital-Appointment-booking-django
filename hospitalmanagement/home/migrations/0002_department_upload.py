# Generated by Django 4.2.5 on 2023-09-23 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='upload',
            field=models.ImageField(default='default_image.jpg', upload_to='department_uploads'),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-23 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dateOfBirth',
            field=models.DateField(default=datetime.date.today),
        ),
    ]

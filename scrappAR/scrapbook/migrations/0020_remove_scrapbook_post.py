# Generated by Django 4.1.4 on 2023-01-25 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0019_topic_scrapbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scrapbook',
            name='post',
        ),
    ]

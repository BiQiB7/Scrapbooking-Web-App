# Generated by Django 4.1.4 on 2023-03-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0028_alter_topic_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrapbook',
            name='cover',
            field=models.ImageField(blank=True, default='blank.png', null=True, upload_to='media/'),
        ),
    ]
# Generated by Django 4.1.4 on 2023-03-25 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0029_scrapbook_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapbook',
            name='cover',
            field=models.ImageField(blank=True, default='blank.png', null=True, upload_to='', verbose_name='Image'),
        ),
    ]

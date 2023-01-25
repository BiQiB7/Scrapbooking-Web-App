# Generated by Django 4.1.4 on 2023-01-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0017_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ManyToManyField(blank=True, null=True, to='scrapbook.image'),
        ),
    ]

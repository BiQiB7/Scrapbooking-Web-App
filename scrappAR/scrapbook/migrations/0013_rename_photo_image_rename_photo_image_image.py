# Generated by Django 4.1.4 on 2023-01-24 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0012_rename_post_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photo',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='photo',
            new_name='image',
        ),
    ]

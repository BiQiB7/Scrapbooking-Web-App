# Generated by Django 4.1.4 on 2023-01-24 08:28

from django.db import migrations
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0002_post_photo_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=django_fields.fields.DefaultStaticImageField(blank=True, default='blank.png', upload_to=''),
        ),
    ]

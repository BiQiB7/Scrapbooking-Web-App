# Generated by Django 4.1.4 on 2023-02-09 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_image_desc_image_followers_image_following_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='pic',
            field=models.ImageField(default='main/media/blank-user.jpg', null=True, upload_to='img/%y'),
        ),
    ]

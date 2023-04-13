# Generated by Django 4.1.4 on 2023-02-10 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0012_alter_image_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='caption',
        ),
        migrations.AddField(
            model_name='image',
            name='job',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
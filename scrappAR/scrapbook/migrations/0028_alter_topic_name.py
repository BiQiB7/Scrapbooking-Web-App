# Generated by Django 4.1.4 on 2023-03-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0027_alter_scrapbook_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
# Generated by Django 4.1.4 on 2023-01-26 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapbook', '0021_remove_scrapbook_topic_posts_scrapbook'),
    ]

    operations = [
        migrations.CreateModel(
            name='select_scrapbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrapbook', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'scrapbooks',
            },
        ),
    ]

# Generated by Django 4.2.6 on 2023-11-06 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_remove_banner_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
    ]

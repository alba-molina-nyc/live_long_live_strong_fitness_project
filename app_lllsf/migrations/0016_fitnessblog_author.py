# Generated by Django 4.2 on 2023-05-01 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lllsf', '0015_rename_image_fitnessblog_image_1_fitnessblog_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessblog',
            name='author',
            field=models.CharField(default='', max_length=255),
        ),
    ]
# Generated by Django 4.2 on 2023-05-13 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_lllsf', '0027_fitnessblog_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeitem',
            name='preview_link',
        ),
    ]
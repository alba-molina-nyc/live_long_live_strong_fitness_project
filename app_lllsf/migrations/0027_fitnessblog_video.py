# Generated by Django 4.2 on 2023-05-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_lllsf', '0026_service_image_service_paragraph_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitnessblog',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]

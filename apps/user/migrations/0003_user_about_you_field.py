# Generated by Django 4.0.6 on 2022-09-04 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_image_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_you_field',
            field=models.TextField(blank=True, null=True, verbose_name='О себе'),
        ),
    ]

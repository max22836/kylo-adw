# Generated by Django 4.0.6 on 2022-08-01 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_created_at_article_tags_article_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=models.ImageField(null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]
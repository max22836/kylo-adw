from django.db import models
from django.utils.safestring import mark_safe
from imagekit.models import ProcessedImageField, ImageSpecField
from pilkit.processors import ResizeToFill
from config.settings import MEDIA_ROOT


class BlogCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    # image = models.ImageField(verbose_name='Изображение', upload_to='blog/category/', null=True)
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/category',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 100},
        null=True
    )

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}' width ='70'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория Блога'
        verbose_name_plural = 'Категории Блога'


class Tag(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'


class Article(models.Model):
    category = models.ForeignKey(
        to=BlogCategory,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True

    )
    tags = models.ManyToManyField(to=Tag, verbose_name='Тэги')
    image = ProcessedImageField(
        verbose_name='Изображение',
        upload_to='blog/article/',
        processors=[],
        format='JPEG',
        options={'quality': 100},
        null=True
    )
    image_thunmbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 1000}
    )
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    text_preview = models.TextField(verbose_name='Текст-превью')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата редактирования', auto_now=True)

    def image_tag_thumbnail(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image_thunmbnail}' width ='70'>")

    image_tag_thumbnail.short_description = 'Текущее изображение'
    image_tag_thumbnail.allow_tags = True

    def image_tag(self):
        if self.image:
            return mark_safe(f"<img src='/{MEDIA_ROOT}{self.image}'>")

    image_tag.short_description = 'Текущее изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

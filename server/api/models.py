import uuid

from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class ArticleCategory(models.Model):
    """文章分类"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField('分类名称', max_length=50)
    children = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name


class ArticleTag(models.Model):
    """标签"""
    name = models.CharField('标签名', max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    """文章"""
    MARKDOWN = 'MD'
    RICH_TEXT = 'RT'
    ARTICLE_CONTENT_TYPE = (
        (MARKDOWN, 'Markdown'),
        (RICH_TEXT, 'RichText'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField('标题', max_length=200)
    summary = models.CharField('简介', max_length=500, default='', blank=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField('文章内容')
    content_type = models.CharField('文章内容类型', choices=ARTICLE_CONTENT_TYPE, default=MARKDOWN, max_length=20)
    tags = models.ManyToManyField(ArticleTag, blank=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    public = models.BooleanField('是否公开', default=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_datetime']


class ImageUploaded(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ImageField(upload_to='images', blank=False, null=False)
    create_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name

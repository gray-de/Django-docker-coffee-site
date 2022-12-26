from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    # author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, verbose_name='Аккаунт')
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True, verbose_name='Контент')
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано:')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Изменено:')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['title']

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug':self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['name']




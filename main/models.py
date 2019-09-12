from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32, db_index=True)
    slug = models.SlugField(max_length=32, db_index=True, unique=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категорія', on_delete=models.CASCADE)
    name = models.CharField(max_length=256, db_index=True, verbose_name='Назва')
    slug = models.SlugField(max_length=256, db_index=True, unique=True)
    image = models.ImageField(upload_to='prod_img/', blank=True, verbose_name='Зображення')
    description = models.TextField(blank=True, verbose_name='Опис')
    short_description = models.TextField(max_length=245, blank=True, verbose_name='Короткий опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    available = models.BooleanField(default=True, verbose_name='Наявність')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Створено')
    updated = models.DateTimeField(auto_now=True, verbose_name='Оновлено')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None, verbose_name='Товар')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name="Користувач")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Створено')
    text = models.TextField(max_length=500, blank=False, verbose_name='Зміст')
    rating = models.IntegerField(choices=RATING_CHOICES, default=5, verbose_name='Рейтинг')

    class Meta:
        verbose_name = 'Відгук'
        verbose_name_plural = 'Відгуки'

    def __str__(self):
        return "%s" % self.user

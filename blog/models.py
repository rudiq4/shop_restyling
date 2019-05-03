from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=32, verbose_name='Імя')
    short_text = models.TextField(max_length=228, verbose_name='Короткий текст(>228)')
    full_text = models.TextField(verbose_name='Повний текст')
    slug = models.SlugField(db_index=True, unique=True)
    image = models.ImageField(upload_to='blog_img/', blank=True, verbose_name='Зображення')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name="Користувач")
    available = models.BooleanField(default=True, verbose_name='Активність')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Створено')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Оновлено')

    class Meta:
        ordering = ['-updated']  # sorted by date of update :D
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('blog:BlogDetail', args=[self.slug])

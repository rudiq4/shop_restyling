from django.db import models
from main.models import Product
from django.contrib.auth.models import User


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Користувач")
    first_name = models.CharField(max_length=32, verbose_name="Ім'я")
    last_name = models.CharField(max_length=32, verbose_name="Прізвище")
    email = models.EmailField(verbose_name='e-mail')
    favorites = models.ManyToManyField(Product, verbose_name="Улюблені товари")

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    def __str__(self):
        return self.user

from django.db import models
from main.models import Product


class Order(models.Model):
    size = models.DecimalField(max_digits=3, decimal_places=1, default=None, verbose_name='Розмір')
    first_name = models.CharField(verbose_name="Ім'я", max_length=50)
    last_name = models.CharField(verbose_name='Прізвище', max_length=50)
    email = models.EmailField(verbose_name='Email')
    city = models.CharField(verbose_name='Місто', max_length=100)
    address = models.CharField(verbose_name='Вулиця, дім', max_length=250)
    postal_code = models.CharField(verbose_name='Поштовий код', max_length=20)
    created = models.DateTimeField(verbose_name='Створено', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Оновлено', auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачене', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'

    def __str__(self):
        return 'Замовлення: {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='Ціна', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name='Кількість', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

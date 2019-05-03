# Generated by Django 2.1.7 on 2019-05-03 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.DecimalField(decimal_places=1, default=None, max_digits=3, verbose_name='Розмір')),
                ('first_name', models.CharField(max_length=50, verbose_name="Ім'я")),
                ('last_name', models.CharField(max_length=50, verbose_name='Прізвище')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('city', models.CharField(max_length=100, verbose_name='Місто')),
                ('address', models.CharField(max_length=250, verbose_name='Вулиця, дім')),
                ('postal_code', models.CharField(max_length=20, verbose_name='Поштовий код')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Оновлено')),
                ('paid', models.BooleanField(default=False, verbose_name='Оплачене')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Кількість')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='main.Product')),
            ],
        ),
    ]

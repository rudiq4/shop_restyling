from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import random


def product_list(request, category_slug=None):
    template = 'shop/product/list.html'
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    page = request.GET.get('page')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        sort_products = products.filter(category=category)
        paginator = Paginator(sort_products, 9)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    else:
        paginator = Paginator(products, 9)
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'page': page
    }
    return render(request, template, context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    template = 'shop/product/detail.html'
    return render_to_response(template,
                              {'product': product,
                               'cart_product_form': cart_product_form})


def test(request):
    print('Рандомна фраза яка буде в консолі')
    template = 'shop/test.html'
    randint = random.randint(0, 10)
    names = ['Zenik', 'Orko', 'Misha', 'Slavko']
    date_and_time = datetime.datetime.now()
    context = {'random_digit': randint,
               'date_and_time': date_and_time,
               'names':names}
    return render(request, template, context)

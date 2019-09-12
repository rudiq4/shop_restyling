from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
#  from .forms import AddReviewForm
from django.urls import reverse
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
    reviews = product.review_set.all()
    template = 'shop/product/detail.html'
    return render_to_response(template,
                              {'product': product,
                               'cart_product_form': cart_product_form,
                               'reviews': reviews})


# def add_comment(request, id):
#     if request.method != 'POST':
#         form = AddReviewForm()
#     else:
#         form = AddReviewForm(request.POST)
#         if form.is_valid():
#             form.save()  # Зберігаємо форму в БД
#             return HttpResponseRedirect(reverse('main'))  # Перенаправляємо Юзера на вказаний урл
#     return render(request, 'new_vehicle.html', locals())


def test(request):
    print('Рандомна фраза яка буде в консолі')
    template = 'shop/test.html'
    randint = random.randint(0, 10)
    names = ['Zenik', 'Orko', 'Misha', 'Slavko']
    date_and_time = datetime.datetime.now()
    context = {'random_digit': randint,
               'date_and_time': date_and_time,
               'names': names}
    return render(request, template, context)

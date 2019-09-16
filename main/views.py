from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect
from django.http import HttpResponse
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from .forms import AddReviewForm
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime
import random
from django.views.generic import View


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


class AddReview(View):
    def get(self, request):
        form = AddReviewForm
        return render(request, 'shop/product/add_review.html', context={'form':form})


# def add_review(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = AddReviewForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('shop/product/list.html')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = AddReviewForm()
#
#     return render(request, 'name.html', {'form': form})


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

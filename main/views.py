from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponseRedirect, redirect
from django.http import HttpResponse
from .models import Category, Product, Review
from cart.forms import CartAddProductForm
from .forms import AddReviewForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        return render(request, 'shop/product/add_review.html', context={'form': form})

    def post(self, request):
        bound_form = AddReviewForm(request.POST)

        if bound_form.is_valid():
            new_review = bound_form.save()
            return redirect('shop:ProductList')
        return render(request, 'shop/product/add_review.html', context={'form': bound_form})

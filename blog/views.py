from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_list(request):
    template = 'blog/blog.html'
    posts = Post.objects.filter(available=True)
    page = request.GET.get('page')
    paginator = Paginator(posts, 9)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'page': page
    }
    return render(request, template, context)


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, available=True)
    template = 'blog/detail.html'
    return render_to_response(template, {'post': post})

from django.conf.urls import url
from .views import *
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
                  path('add_review/', AddReview.as_view(), name='add_review'),
                  url(r'^test/$', views.test, name='test'),
                  url(r'^$', views.product_list, name='ProductList'),
                  url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='ProductListByCategory'),
                  url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='ProductDetail'),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

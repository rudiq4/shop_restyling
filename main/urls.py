from django.conf.urls import url
from .views import *
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'main'

urlpatterns = [
                  path('add_review/', AddReview.as_view(), name='add_review'),
                  url(r'^$', views.product_list, name='ProductList'),
                  url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='ProductListByCategory'),
                  url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='ProductDetail'),
                  url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
                  url(r'^calendar/(?P<name>\w+)/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{1,2})$',
                      views.calendar),
              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

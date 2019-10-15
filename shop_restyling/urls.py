from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop_restyling'

urlpatterns = [
                  url(r'^admin/', admin.site.urls, name='admin'),
                  url(r'^chaining/', include('smart_selects.urls')),
                  url(r'^chaining/', include('smart_selects.urls')),
                  url(r'^cart/', include('cart.urls', namespace='cart')),
                  url(r'^blog/', include('blog.urls', namespace='blog')),
                  url(r'^', include('main.urls', namespace='shop')),
                  url(r'^order/', include('orders.urls', namespace='orders')),
                  url(r'^customer/', include('customer.urls', namespace='customer')),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
                  # url(r'^test/$', views.test, name='test'),
                  url(r'^$', views.blog, name='Blogg'),
                  # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.blog_detail, name='BlogDetail'),

              ] \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

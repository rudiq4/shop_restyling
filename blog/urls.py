from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog_app'

urlpatterns = [
    url(r'^$', views.blog_list, name='BlogList'),
    url(r'^(?P<slug>[-\w]+)/$', views.blog_detail, name='BlogDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


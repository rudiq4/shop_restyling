from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'customer'

urlpatterns = [
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    # url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^account/(?P<user>[-\w]+)/$', views.AccountView.as_view(), name='account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

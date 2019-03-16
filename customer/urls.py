from django.conf.urls import url
from . import views


app_name = 'customer'

urlpatterns = [
    url(r'^registration/$', views.RegistrationView.as_view(), name='registration'),
]

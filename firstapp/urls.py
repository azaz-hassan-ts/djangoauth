from django.conf.urls import url
from . import views

urlpatterns = [
    url('first', views.first, name='first')
]
from django.urls import path
from . import views
from django.conf.urls import url

app_name='store'

urlpatterns=[
    path("", views.home, name="home"),
    path("cart/<item_id>", views.add_to_cart, name="add-to-cart"),
]
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
	path("create/", views.order_create, name='order_create'),
	path("buynow/<product_id>", views.buy_now, name='buy_now'),
]

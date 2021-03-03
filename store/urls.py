from django.urls import path
from . import views
from django.conf.urls import url

app_name='store'

urlpatterns=[
    # path("", views.home, name="home"),
    # path("cart/<item_id>", views.add_to_cart, name="add-to-cart"),
    path("", views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.product_detail, name='product_detail'),
]
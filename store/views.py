from django.shortcuts import render
from .models import Item,OrderItem,Order
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

from django.views.generic import ListView, DetailView, View
# Create your views here.

def home(request):
    context= {
        'items': Item.objects.all()
    }
    print(context)
    return render(request,'registration/home.html',context)    

# def add_to_cart(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     order_item = OrderItem.objects.create(Item=Item)
#     order_qs = Order.objects.filter(user=request.user, ordered=False)
#     if order_qs.exists():
#         order = order_qs[0]
#         if order.items.filter(item__slug=item.slug).exists():
#             order_item.quantity += 1
#             order_item.save()
#             # messages.info(request, "This item quantity was updated.")
#             # return redirect("order-summary")
#         else:
#             order= Order.objects.create(user=request.user)
#             order.items.add(order_item)
#             # messages.info(request, "This item was added to your cart.")
#             return redirect("store:product",slug=slug)

#     else:

#         ordered_date = timezone.now()
#         order = Order.objects.create(
#             user=request.user, ordered_date=ordered_date)
#         order.items.add(order_item)
#         messages.info(request, "This item was added to your cart.")
#         return redirect("product-detail", slug=item.slug)

@login_required
def add_to_cart(request,item_id):
    item = get_object_or_404(Item, pk=item_id)
    cart= OrderItem.objects.get_or_create(user=request.user)
    order,created = OrderItem.objects.get_or_create(item=item,cart=cart)
    order.quantity += 1
    order.save()
    messages.success(request, "Cart updated!")
    # return redirect('cart')
    return render(request,'store/cart.html')


def checkout(request):
    context={}
    return render(request,'store/checkout.html')
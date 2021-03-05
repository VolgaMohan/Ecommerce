from django.shortcuts import render,get_object_or_404
from .models import Product
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
        context = {
        'form':form,
        'cart':cart
        }
    return render(request, 'orders/order/create.html', context = context)

def buy_now(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
        return render(request, 'orders/order/created.html', {'order': order})
    else:
        product = get_object_or_404(Product, id=product_id)
        print(product)
        form = OrderCreateForm()
        context = {
        'form':form,
        'product':product
        }
        return render(request, 'orders/order/create.html', context = context)
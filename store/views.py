from .models import Category, Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
# from .models import Item,OrderItem,Order,
# Create your views here.

def product_list(request, category_slug=None):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = Product.objects.filter(category=category)

	context = {
		'category': category,
		'categories': categories,
		'products': products
	}
	return render(request, 'store/product/list.html', context)


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	cart_product_form = CartAddProductForm()
	context = {
		'product': product,
		'cart_product_form': cart_product_form
	}
	return render(request, 'store/product/detail.html', context)


# def home(request):
#     context= {
#         'items': Item.objects.all()
#     }
#     print(context)
#     return render(request,'registration/home.html',context)    

# @login_required
# def add_to_cart(request,item_id):
#     item = get_object_or_404(Item, pk=item_id)
#     cart= OrderItem.objects.get_or_create(user=request.user)
#     order,created = OrderItem.objects.get_or_create(item=item,cart=cart)
#     order.quantity += 1
#     order.save()
#     messages.success(request, "Cart updated!")
#     # return redirect('cart')
#     return render(request,'store/cart.html')


# def checkout(request):
#     context={}
#     return render(request,'store/checkout.html')

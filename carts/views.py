from django.shortcuts import render, redirect

# Create your views here.

def _cart_id(requst):
    cart = request.session.session_key
    if not cart:
        cart = requst.session.create()
    return cart

def add_to_cart(request, product_id):
    product = Product.objects.get(product_id)
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
    except cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product = product, cart = cart)
        cart_item.quantity += 1
        cart_item.save()
    except cart_item.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart
        )
        cart_item.save()
    return redirect('cart')

def cart(request):
    return render(request, 'store/cart.html')
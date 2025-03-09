from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Products
from django.http import JsonResponse



def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()
    return render(request, 'cart_summary.html', {'cart_products':cart_products,'quantities':quantities, 'totals':totals})



def cart_add(request):
    # التحقق من نوع الطلب
    if request.method == 'POST':
        # التحقق من وجود مفتاح 'product_id' في البيانات
        product_id = int(request.POST.get('product_id'))
        product_qty= int(request.POST.get('product_qty'))

        if not product_id:
            return JsonResponse({'error': 'No product ID provided'}, status=400)

        try:
            # تحويل product_id إلى عدد صحيح
            product_id = int(product_id)
        except ValueError:
            return JsonResponse({'error': 'Invalid product ID'}, status=400)

        # الحصول على المنتج بناءً على الـ id
        product = get_object_or_404(Products, id=product_id)

        # إضافة المنتج إلى السلة
        cart = Cart(request)
        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()
        # إرسال استجابة JSON تحتوي على اسم المنتج
        #response = JsonResponse({'product_title': product.title})
        response = JsonResponse({'qty':product_qty, 'product_id':product_id})
        return response
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def cart_delete(request):
    cart =Cart(request)
    if request.method == 'POST':
        # التحقق من وجود مفتاح 'product_id' في البيانات
        product_id = int(request.POST.get('product_id'))

        cart.delete(product=product_id)
        response = JsonResponse({'product_id':product_id})
        return response
        #return redirect('cart_summary')




def cart_update(request):
    cart =Cart(request)
    if request.method == 'POST':
        # التحقق من وجود مفتاح 'product_id' في البيانات
        product_id = int(request.POST.get('product_id'))
        product_qty= int(request.POST.get('product_qty'))
        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty':product_qty})
        return response
        #return redirect('cart_summary')
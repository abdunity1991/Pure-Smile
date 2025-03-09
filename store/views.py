from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserform, ChangePasswordForm, UserInfoForm
from payment.forms import ShippingForm
from payment.models import ShippingAddress
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import ChangePasswordForm
from django.db.models import Q
import json
from cart.cart import Cart


def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        searched = Products.objects.filter(Q(title__icontains=searched) | Q(desc__icontains=searched))
        if not searched:
            messages.success(request, 'لا يوجد منتج بهذا الاسم')
            return render(request, 'search.html', {})
        else:
            return render(request, 'search.html', {'searched':searched})
    else:
        return render(request, 'search.html', {})

def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if form.is_valid() or shipping_form .is_valid():
            form.save()
            shipping_form.save()
            print('معلوماتك تم تحديثها')
            return redirect('index')
        return render(request, 'update_info.html',{'form':form, 'shipping_form':shipping_form})
    else:
        print('لم يتم تحديث البيانات اسف ')
        return redirect('index')

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user

        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                # إعادة تسجيل الدخول بعد تغيير كلمة المرور (إذا أردت ذلك)
                login(request, current_user)
                return redirect('update_user')
            else:
                # عرض الأخطاء في حالة كان النموذج غير صالح
                for error in list(form.errors.values()):
                    #messages.error(request, error)
                    print((request, error))
                    # إرجاع الصفحة نفسها مع النموذج والأخطاء
                    return redirect('update_password')

        else:
            form = ChangePasswordForm(current_user)
            return render(request, 'update_password.html', {'form': form})

    else:
        print('User is not authenticated')
        return redirect('index')

def update_user(request):
    
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserform(request.POST or None, instance=current_user)

        if user_form.is_valid():
            user_form.save()

            login (request, current_user)
            print('done to update')

            return redirect('index')
        return render(request, 'update_user.html',{'user_form':user_form})
    else:
        print('Sorrrrrry.............')
        return redirect('innex')

def category_view(request, foo):
    foo = foo.replace('-', '')
    try:
        category = Category.objects.get(name=foo)
        products = Products.objects.filter(category=category)
        return render(request, 'category.html', {'products':products, 'category':category})
    except:
        messages.success(request, 'لم يتم الانتقال بشكل صحيح')
        return redirect('index')
        
def product_view(request, pk):
    product = Products.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def index(request):
    products = Products.objects.all()
    return render(request, 'index.html', {'products':products})

def cart(request):
    return render(request, 'cart.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request,user)
            current_user = Profile.objects.get(user__id=request.user.id)
            saved_cart = current_user.old_cart
            if saved_cart:
                converted_cart = json.loads(saved_cart)
                cart = Cart(request)         
                
                for key,value in converted_cart.items():
                    cart.db_add(product=key, quantity=value)

          
            messages.success(request,('لقد قمت بتسجيل الدخول '))
            return redirect('index')
        else:
            messages.success(request,('يوجد خطأ يرجى المحاولة ثانية'))
            return redirect('login')     
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('لقد سجلت خروجك شكرا لوجودك معنا '))
    return redirect('login')

def accounts_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # loginuser
            user = authenticate(username=username, password=password)
            login(request, user)
            print('لقد انشأت حساب جديد بنجاح ')
            return redirect('update_info')
        else:
            messages.success(request, ('لم يتم انشاء الحساب لوجود خطأ'))
            return redirect('accounts')
    else:
        return render(request, 'account.html', {'form':form}) 
    





#S@f3P@ss!20211
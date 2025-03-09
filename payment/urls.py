from . import views
from django.urls import path

urlpatterns = [
    path('payment_success', views.payment_success, name='payment_success'),
    path('chekout', views.chekout, name='chekout'),
    path('billing_info', views.billing_info, name='billing_info'),


]

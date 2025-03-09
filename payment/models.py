from django.db import models
from django.contrib.auth.models import User
from store.models import Products
from django.db.models.signals import post_save



class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank= True)
    shipping_name = models.CharField(max_length=200)
    shipping_phone = models.CharField(max_length=20, blank=True, null=True)
    shipping_address1 = models.TextField(max_length=15000)
    shipping_address2 = models.TextField(max_length=15000, blank=True, null=True)
    shipping_city = models.CharField(max_length=20, blank=True, null=True)
    shipping_avaleble = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Shipping Address"


    def __str__(self):
        return f'Shipping Address - {str(self.id)}'


def creat_shipping(sender, instance, created, **kwargs):
    if created:
        user_shipping = ShippingAddress(user=instance)
        user_shipping.save()

post_save.connect(creat_shipping, sender=User)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank= True)
    fullnam = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address1 = models.TextField(max_length=15000)
    avaleble = models.CharField(max_length=150)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    date_order = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'Order - {str(self.id)}'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True )
    Product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank= True)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f'Order Item - {str(self.id)}'
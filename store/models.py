from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modefied = models.DateTimeField(User, auto_now=True)
    phone = models.CharField(max_length=20, blank=True)
    address1 = models.CharField(max_length=200, blank=True)
    address2 = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=20, blank=True)
    avaleble = models.CharField(max_length=150, blank=True)
    old_cart = models.CharField(max_length=5000, blank=True, null= True)


    def __str__(self):
        return self.user.username

def creat_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(creat_profile, sender=User)




class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Products(models.Model):
    img = models.ImageField(upload_to='uploads/product/')#, null=True, blank=True
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places= 2)
    desc = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
    
class Order(models.Model):
    pr = models.ForeignKey(Products, on_delete=models.CASCADE, default=1)
    quantity =  models.IntegerField(default=1)
    address = models.CharField(max_length=150, default='', blank=True, )
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.pr.title
    
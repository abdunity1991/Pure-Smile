from django.contrib import admin
from .models import *




admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(Profile)




class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    filed = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInLine]


admin.site.unregister(User)


admin.site.register(User, UserAdmin)
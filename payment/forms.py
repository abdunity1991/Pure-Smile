from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):

    shipping_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'الاسم الكامل'}), required=True)
    shipping_phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}), required=True)
    shipping_address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'العنوان الاول'}), required=True)
    shipping_address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'العنوان الثاني'}), required=False)
    shipping_city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'المدينة'}), required=False)
    shipping_avaleble = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'اوقات التواجد'}), required=True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_name', 'shipping_phone', 'shipping_address1', 'shipping_address2',
                   'shipping_city', 'shipping_avaleble']
        exclude= ['user']
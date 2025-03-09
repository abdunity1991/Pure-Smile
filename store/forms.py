from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile




class UserInfoForm(forms.ModelForm):
	phone = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone'}), required=False)
	address1 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address1'}), required=False)
	address2 = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address2'}), required=False)
	city = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'city'}), required=False)
	avaleble = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'avaleble'}), required=False)

	class Meta:
		model = Profile
		fields = ('phone', 'address1', 'address2', 'city', 'avaleble')


class ChangePasswordForm(SetPasswordForm):
	class Meta:
		model = User
		fileds = ['new_password1', 'new_password2']


	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class UpdateUserform(UserChangeForm):
    password = None
    # حقل الاسم الأول مع النصوص باللغة العربية
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأول'}), 
        required=False
    )
    # حقل الاسم الأخير مع النصوص باللغة العربية
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأخير'}), 
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super(UpdateUserform, self).__init__(*args, **kwargs)

        # تخصيص الحقول هنا لتشمل اللغة العربية في الإرشادات
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'اسم المستخدم'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>مطلوب. 150 حرفًا أو أقل. فقط الحروف، الأرقام و@/./+/-/_ مسموحة.</small></span>'
        )

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'الاسم الأول'
        self.fields['first_name'].label = ''

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'الاسم الأخير'
        self.fields['last_name'].label = ''



class SignUpForm(UserCreationForm):
    # حقول الاسم الأول والاسم الأخير مع النصوص باللغة العربية
    first_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأول'}), 
        required=False
    )
    last_name = forms.CharField(
        label="", 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'الاسم الأخير'}), 
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        # تخصيص الحقول هنا لتشمل اللغة العربية في الإرشادات
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'اسم المستخدم'
        self.fields['username'].label = ''
        self.fields['username'].help_text = (
            '<span class="form-text text-muted"><small>مطلوب. 150 حرفًا أو أقل. فقط الحروف، الأرقام و@/./+/-/_ مسموحة. مثال عبدالرحمن-1991 لا تستعمل الفراغ بالاسم</small></span>'
        )

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'كلمة المرور'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = (
            '<ul class="form-text text-muted small">'
            '<li>لا يمكن أن تكون كلمة المرور مشابهة للمعلومات الشخصية الأخرى.</li>'
            '<li>يجب أن تحتوي كلمة المرور على 8 أحرف على الأقل.</li>'
            '<li>لا يمكن أن تكون كلمة المرور كلمة مرور شائعة.</li>'
            '<li>لا يمكن أن تكون كلمة المرور رقمية بالكامل.</li>'
            '</ul>'
        )

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'تأكيد كلمة المرور'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = (
            '<span class="form-text text-muted"><small>أدخل نفس كلمة المرور للتحقق.</small></span>'
        )
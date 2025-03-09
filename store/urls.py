from . import views
from django.urls import path

urlpatterns = [
    path('', views.login_user, name='login'),
    path('index/', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('accounts/', views.accounts_user, name='accounts'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('product/<int:pk>/', views.product_view, name='product'),
    path('category/<str:foo>', views.category_view, name='category'),
    path('search', views.search, name='search'),
]

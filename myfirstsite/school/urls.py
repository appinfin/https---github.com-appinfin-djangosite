from django.urls import path, re_path
from .views import *

# допустимые адреса

urlpatterns = [
    # path('', index, name='home'),
    path('', ProductHome.as_view(), name='home'),
    path('about/', about, name='about'),
    # path('add_post/', add_post, name='add_post'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # path('products/<int:products_id>/', products, name='products'),
    path('product_description/<slug:prodid>/', product_description, name='product_description'),
    
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'), #путь с регуляркой
]
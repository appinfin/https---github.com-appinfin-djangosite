from django.urls import path, re_path
from .views import *

# допустимые адреса

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_post/', add_post, name='add_post'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('prod/<int:prodid>/', products),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'),
]
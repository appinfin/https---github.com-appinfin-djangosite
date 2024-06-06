from django import template
from school.models import *

register = template.Library()

def get_product():
    return Product.objects.all()
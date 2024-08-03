from django import template
from school.models import Product

register = template.Library()

@register.simple_tag()
def get_product():
    return Product.objects.all()
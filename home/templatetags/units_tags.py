from django import template
from workers.models import Units
register = template.Library()
@register.simple_tag(name='my_tag')
def units_total():
    return Units.objects.count()
@register.inclusion_tag('home/units.html')
def units_all():
    units = Units.objects.all().order_by('id')[1:]
    unit=Units.objects.first()
    return locals()
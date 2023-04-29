from django import template
from vacancies.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_profession(filter=None):
    if not filter:
         return Profession.objects.all()
    else:
        return Profession.objects.filter(pk=filter)

@register.inclusion_tag('vacancies/list_categories.html')
def show_profession(sort:None, cat_selected=0):
    if not sort:
        cats = Profession.objects.all()
    else:
        cats = Profession.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}
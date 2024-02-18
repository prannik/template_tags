from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag('header.html', takes_context=True)
def show_header(context):
    menu_items = Menu.objects.all()

    return {
        'menu_items': menu_items,
    }

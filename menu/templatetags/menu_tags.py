from django import template
from menu.models import Menu

register = template.Library()


@register.inclusion_tag(filename='menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']

    try:
        menu = Menu.objects.get(name=menu_name)
        menu_items = menu.items.filter(parent=None)

    except Menu.DoesNotExist:
        menu_items = []

    return {
        'menu_items': menu_items,
        'request': request,
    }

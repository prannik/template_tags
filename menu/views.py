from django.shortcuts import render
from .models import Menu


def menu_items(request, menu_name):
    try:
        menu = Menu.objects.get(name=menu_name)
        items = menu.items.all()
        url_menu = str(request.path).replace('/', '')

    except Menu.DoesNotExist:
        items = None

    return render(request, template_name='base.html', context={'menu_items': items, 'url_menu': url_menu})

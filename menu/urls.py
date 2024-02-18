from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path(
        '<str:menu_name>/',
        views.menu_items, name='menu_items'
    ),
]

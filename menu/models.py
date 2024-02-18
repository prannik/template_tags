from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    url = models.SlugField(verbose_name='Url', max_length=256)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu Items'

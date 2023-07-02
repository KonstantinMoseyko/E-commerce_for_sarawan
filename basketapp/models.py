from django.db import models
from django.conf import settings
from store.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='кол-во товара', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    # Общая стоимость одной позиции 
    @property
    def product_cost(self):
        return self.product.price * self.quantity

    # общее количество товара по всем заказам в корзине
    @property
    def total_quantity(self):
        _product = Basket.objects.filter(user=self.user)
        _total_quantity = sum(list(map(lambda x: x.quantity, _product)))
        return _total_quantity

    # общая стоимость всех предложений пользователя в корзине
    @property
    def total_cost(self):
        _product = Basket.objects.filter(user=self.user)
        _total_cost = sum(list(map(lambda x: x.product_cost, _product)))
        return _total_cost

    # количество заказов пользователя в корзине
    @staticmethod
    def get_items(user):
        return user.basket.select_related()
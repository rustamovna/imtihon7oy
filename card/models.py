from django.db import models
from django.conf import settings
from products.models import Product
# Create your models here.

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="card_carts")

    def __str__(self):
        return f"{self.user.username} savati"

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='card_cartitems')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.quantity} dona"

    @property
    def total_price(self):
        return self.product.price * self.quantity

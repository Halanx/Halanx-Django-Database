
from django.contrib import admin
from Carts.models import CartItem
from Carts.models import Cart


admin.site.register(Cart)
admin.site.register(CartItem)


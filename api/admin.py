from django.contrib import admin
from .models import User, Cart, Product, Order

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Order)

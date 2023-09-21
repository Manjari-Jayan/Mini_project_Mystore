from django.contrib import admin
from .models import Carousel, Cart
from .models import Category, Subcategory
from .models import UserProfile

from .models import Product
admin.site.register(Product)
# admin.site.register(SubProduct)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Carousel)
admin.site.register(UserProfile)
admin.site.register(Cart)
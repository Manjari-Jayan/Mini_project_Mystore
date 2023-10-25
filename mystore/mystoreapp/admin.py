from django.contrib import admin
from .models import Carousel, Cart, ComparisonList, WishlistItem
from .models import Category, Subcategory, Series
from .models import UserProfile
from .models import Product


admin.site.register(Product)
# admin.site.register(SubProduct)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Series)
admin.site.register(Carousel)
admin.site.register(UserProfile)
admin.site.register(Cart)
admin.site.register(WishlistItem)
admin.site.register(ComparisonList)

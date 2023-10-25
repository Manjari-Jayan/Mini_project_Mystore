from django.db import models

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Series(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    brand = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    series = models.ForeignKey(Series, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    discount = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    stock = models.PositiveIntegerField(default=0)

    processor = models.CharField(max_length=100, null=True, blank=True)
    front_camera = models.CharField(max_length=100, null=True, blank=True)
    back_camera = models.CharField(max_length=100, null=True, blank=True)
    ram = models.CharField(max_length=100, null=True, blank=True)
    rom = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return self.name
    
# class SubProduct(models.Model):
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=100, null=True, blank=True)
#     image = models.FileField(null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     price = models.CharField(max_length=100, null=True, blank=True)
#     discount = models.CharField(max_length=100, null=True, blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
    
    
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.FileField(null=True, blank=True)
   
    def __str__(self):
        return self.user.username
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.TextField(default={'objects': []}, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    

# models.py


from django.db.models.signals import post_save
from django.dispatch import receiver

class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Assuming you have a Product model
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"
    

class ComparisonList(models.Model):
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f"Comparison List {self.id}"
    



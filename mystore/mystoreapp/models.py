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
    
from django.db import models
from django.contrib.auth.models import User

# class Cart(models.Model):
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     # Assuming you want to store a list of product IDs in the cart
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return str(self.user.username)

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
    


# mystoreapp/models.py
# mystoreapp/models.py

# mystoreapp/forms.py

# from django import forms
# from .models import DeliveryAgent
 # Remove this line

# class DeliveryAgentForm(forms.ModelForm):
#     class Meta:
#         model = DeliveryAgent
#         fields = ['agent_name', 'place', 'pincode', 'mobile']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # You can customize the form widgets or add additional validation here if needed
    



# class BillingDetails(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # If you want to associate the billing details with a user
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     street_address = models.CharField(max_length=255)
#     apartment_suite_unit = models.CharField(max_length=255, blank=True, null=True)  # Optional field
#     town_city = models.CharField(max_length=255)
#     postcode_zip = models.CharField(max_length=20)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()

#     def _str_(self):
#         return f"{self.first_name} {self.last_name}'s Billing Details"


ORDERSTATUS = ((1, "Pending"), (2, "Dispatch"), (3, "On the way"), (4, "Delivered"), (5, "Cancel"), (6, "Return"))

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.TextField(default={'objects': []}, null=True, blank=True)
    total = models.CharField(max_length=100, null=True, blank=True)
    status = models.IntegerField(choices=ORDERSTATUS, default=1)
    
    # Additional Fields
    state = models.CharField(max_length=100, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    apartment_suite_unit = models.CharField(max_length=50, null=True, blank=True)
    town_city = models.CharField(max_length=100, null=True, blank=True)
    postcode_zip = models.CharField(max_length=20, null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    




class DeliveryAgent(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    AVAILABILITY_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='delivery_agent')
    name = models.CharField(max_length=255, default=None, blank=True, null=True)

    username = models.CharField(max_length=30, default=None, blank=True, null=True)  # Added username field
    # email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, default=None, blank=True, null=True)
    # license_number = models.CharField(max_length=20,unique=True)
    license_number = models.CharField(max_length=20, unique=True, default=None, blank=True, null=True)

    vechicle_type = models.CharField(max_length=255,default=1)
    location = models.CharField(max_length=255, default=None, blank=True, null=True)
    password = models.CharField(max_length=255, default=None, blank=True, null=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default='not_available')
    email = models.EmailField(unique=True, default="manjarijayan2024@gmail.com")



    def __str__(self):
        return self.name
    
    def is_approved(self):
        return self.status == 'approved'

    

# class DeliveryAgent(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     place = models.CharField(max_length=100, blank=True, null=True)
#     pincode = models.CharField(max_length=10, blank=True, null=True)
#     location = models.CharField(max_length=100, blank=True, null=True)
#     # assigned_seller = models.ForeignKey(Seller, on_delete=models.CASCADE, null=True, blank=True)
#     latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
#     distance = models.FloatField(null=True, blank=True)
#     is_available = models.BooleanField(default=True)
#     mobile = models.CharField(max_length=100, null=True, blank=True)
#     # assigned_route = models.ForeignKey(Route, null=True, blank=True, on_delete=models.SET_NULL)
#     def __str__(self):
#         return self.user.email


STATUS = ((1, "Read"), (2, "Unread"))
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username



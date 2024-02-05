from collections import OrderedDict
from decimal import Decimal
from gettext import translation
import json
import django
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User
from .models import ORDERSTATUS, Booking, Product
from django.contrib.auth.decorators import login_required
from .models import DeliveryAgent
from django.shortcuts import render, redirect

from decimal import Decimal
from django.conf import settings
from .models import Cart
from mystoreapp.models import Product


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}

        subcategories = Subcategory.objects.filter(category=category)

       
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
    
    for c in nested_categories:
        for s in c.values():
            print(s)
    products = Product.objects.all()
    return render(request,'home.html',{'nested_categories': nested_categories, 'products': products})

def index(request):
    return render(request, 'navigation.html')

def three(request):
    return render(request, '3d.html')

def about(request):
    return render(request, 'about.html')

from .models import Carousel, Cart, Series, Subcategory, UserProfile
def main(request):
    data = Carousel.objects.all()
    dic = {'data':data}
    allcategory = Category.objects.all()
    return render(request, 'index.html', locals())

# def delivery_agent(request):
#     return render(request, 'view_assigned_orders.html')

# <------------------------------------------------Category------------------------

from .models import Category
def add_category(request):
    if request.method == "POST":
        name = request.POST['name']
        
        # Check if the category already exists
        if Category.objects.filter(name=name).exists():
            category_exist_msg = "Category already exists"
        else:
            # Category doesn't exist, create it
            Category.objects.create(name=name)
            category_added_msg = "Category added successfully"   
    return render(request, 'add_category.html', locals())


def view_category(request):
    category = Category.objects.all()
    return render(request, 'view_category.html', locals())

 
def edit_category(request, pid):
    category = Category.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        category.name = name
        category.save()
        msg = "Category Updated"
    return render(request, 'edit_category.html', locals())

def delete_category(request, pid):
    category = Category.objects.get(id=pid)
    category.delete()
    return redirect('view_category')


# <!--------------------------Subcategory--------->

from mystoreapp.models import Category  # Import your Category model

def add_subcategory(request):
    categories = Category.objects.all()
    
    if request.method == "POST":
        name = request.POST['name']
        cat = request.POST['category']
        category = Category.objects.get(id=cat)
        
        # Check if the brand name already exists
        if Subcategory.objects.filter(name=name, category=category).exists():
            messages.error(request, "Brand already exists", extra_tags='brand-exists')
        else:
            Subcategory.objects.create(name=name, category=category)
            messages.success(request, "Brand added successfully", extra_tags='brand-created')

    return render(request, 'add_subcategory.html', {'categories': categories})


def edit_subcategory(request, pid):
    subcategory = Subcategory.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        subcategory.name = name
        subcategory.save()
        msg = "Sub Category Updated"
    return render(request, 'edit_subcategory.html', locals())

def delete_subcategory(request, pid):
    subcategory = Subcategory.objects.get(id=pid)
    subcategory.delete()
    return redirect('view_subcategory')

def view_subcategory(request):
    subcategory = Subcategory.objects.all()
    return render(request, 'view_subcategory.html', locals())

#--------------------------------Series-----------------------------------
def add_series(request):
    category = Category.objects.all()
    brand = Subcategory.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        cat = request.POST['category']
        brandid = request.POST['brand']
        category = Category.objects.get(id=cat)
        brand = Subcategory.objects.get(id=brandid)
        Series.objects.create(name=name,category=category,brand=brand)
        messages.success(request, "Series added")
        catobj = Category.objects.get(id=cat)
        brandobj = Subcategory.objects.get(id=brandid)
        return redirect('view_series')
    return render(request, 'add_series.html', locals())

def edit_series(request, pid):
    series = Series.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        series.name = name
        series.save()
        msg = "Series Updated"
    return render(request, 'edit_series.html', locals())

def delete_series(request, pid):
    series = Series.objects.get(id=pid)
    series.delete()
    return redirect('view_series')

def view_series(request):
    series = Series.objects.all()
    return render(request, 'view_series.html', locals())


# ------------------------------------------Product-------------------

from .models import Product
def add_product(request):
    category = Category.objects.all()
    brand = Subcategory.objects.all()
    series = Series.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        cat = request.POST['category']
        brandid = request.POST['brand']
        seriesid = request.POST['series']
        discount = request.POST['discount']
        desc = request.POST['desc']
        stock = request.POST['stock']
        image = request.FILES['image']
        # New fields
        processor = request.POST['processor']
        front_camera = request.POST['front_camera']
        back_camera = request.POST['back_camera']
        ram = request.POST['ram']
        rom = request.POST['rom']
        catobj = Category.objects.get(id=cat)
        brandobj = Subcategory.objects.get(id=brandid)
        seriesobj = Series.objects.get(id=seriesid)
        # Create a new Product object with the additional fields
        product = Product.objects.create(
            name=name,
            price=price,
            discount=discount,
            category=catobj,
            brand=brandobj,
            series=seriesobj,
            description=desc,
            image=image,
            stock=stock,
            processor=processor,
            front_camera=front_camera,
            back_camera=back_camera,
            ram=ram,
            rom=rom
        )
        messages.success(request, "Product added")
    return render(request, 'add_product.html', locals())

def view_product(request):
    product = Product.objects.all()
    return render(request, 'view_product.html', locals())

def edit_product(request, pid):
    product = Product.objects.get(id=pid)
    category = Category.objects.all()
    brand = Subcategory.objects.all()
    series = Series.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        cat = request.POST['category']
        brandid = request.POST['brand']
        seriesid = request.POST['series']
        discount = request.POST['discount']
        desc = request.POST['desc']
        processor = request.POST['processor']
        front_camera=request.POST['front_camera']
        back_camera=request.POST['back_camera']
        ram=request.POST['ram']
        rom=request.POST['rom']
        stock = request.POST['stock']
        try:
            image = request.FILES['image']
            product.image = image
            product.save()
        except:
            pass
        catobj = Category.objects.get(id=cat)
        brandobj = Subcategory.objects.get(id=brandid)
        seriesobj = Series.objects.get(id=seriesid)
        Product.objects.filter(id=pid).update(
            name=name, price=price, discount=discount, category=catobj, brand=brandobj, series=seriesobj, description=desc, stock=stock, processor=processor,
            front_camera=front_camera,
            back_camera=back_camera,
            ram=ram,
            rom=rom, )
        messages.success(request, "Product Updated")
        return redirect('view_product')
    return render(request, 'edit_product.html', locals())


def delete_product(request, pid):
    product = Product.objects.get(id=pid)
    product.delete()
    messages.success(request, "Product Deleted")
    return redirect('view_product')


# --------------------------------------------add_subproduct such as series ----------------------
# from .models import SubProduct
# def add_subproduct(request):
#     subcategory = Subcategory.objects.all()
#     if request.method == "POST":
#         name = request.POST['name']
#         price = request.POST['price']
#         subcat = request.POST['subcategory']
#         discount = request.POST['discount']
#         desc = request.POST['desc']
#         image = request.FILES['image']
#         subcatobj = Subcategory.objects.get(id=subcat)
#         SubProduct.objects.create(name=name, price=price, discount=discount, subcategory=subcatobj, description=desc, image=image)
#         messages.success(request, "SubProduct added")
#     return render(request, 'add_subproduct.html', locals())

# def view_subproduct(request):
#     subproduct = SubProduct.objects.all()
#     return render(request, 'view_subproduct.html', locals())

# def edit_subproduct(request, pid):
#     subproduct = SubProduct.objects.get(id=pid)
#     subcategory = Subcategory.objects.all()
#     if request.method == "POST":
#         name = request.POST['name']
#         price = request.POST['price']
#         subcat = request.POST['subcategory']
#         discount = request.POST['discount']
#         desc = request.POST['desc']
#         try:
#             image = request.FILES['image']
#             subproduct.image = image
#             subproduct.save()
#         except:
#             pass
#         subcatobj = Subcategory.objects.get(id=subcat)
#         SubProduct.objects.filter(id=pid).update(name=name, price=price, discount=discount, subcategory=subcatobj, description=desc)
#         messages.success(request, "Product Updated")
#     return render(request, 'edit_product.html', locals())


# def delete_subproduct(request, pid):
#     subproduct = SubProduct.objects.get(id=pid)
#     subproduct.delete()
#     messages.success(request, "Product Deleted")
#     return redirect('view_subproduct')




from .models import UserProfile
from django.contrib.auth.decorators import login_required



def user_product(request,pid):
    if pid == 0:
        product = Product.objects.all()
    else:
        category = Category.objects.get(id=pid)
        product = Product.objects.filter(category=category)       
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}

        subcategories = Subcategory.objects.filter(category=category)
       
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
    
    for c in nested_categories:
        for s in c.values():
            print(s)
    products = Product.objects.all()
    return render(request, "user-product.html", locals())

def brand_product(request,pid):   
    subcategory = Subcategory.objects.get(id=pid)
    product = Product.objects.filter(brand=subcategory)       
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}
        subcategories = Subcategory.objects.filter(category=category)      
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
    
    for c in nested_categories:
        for s in c.values():
            print(s)
    products = Product.objects.all()
    return render(request, "brand.html", locals())


def series_product(request,pid):
    series = Series.objects.get(id=pid)
    product = Product.objects.filter(series=series)          
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}

        subcategories = Subcategory.objects.filter(category=category)

       
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
    
    for c in nested_categories:
        for s in c.values():
            print(s)
    products = Product.objects.all()
    return render(request, "series.html", locals())


from django.http import HttpResponse, HttpResponseRedirect
def product_detail(request, pid):
    try:
        product = Product.objects.get(id=pid)
        latest_product = Product.objects.filter().exclude(id=pid).order_by('-id')[:10]
        allcategory = Category.objects.all()
        nested_categories = []
        for category in allcategory:
            category_dict = {'category': category, 'subcategories': []}

            subcategories = Subcategory.objects.filter(category=category)      
            for subcategory in subcategories:
                    subcategory_dict = {'subcategory': subcategory, 'series': []}
                   # Retrieve series for this subcategory
                    series = Series.objects.filter(brand=subcategory)
                    for s in series:
                        subcategory_dict['series'].append(s)
                    category_dict['subcategories'].append(subcategory_dict)
            nested_categories.append(category_dict)        
        for c in nested_categories:
            for s in c.values():
                print(s)
        products = Product.objects.all()
        in_stock = product.stock > 0
        if request.method == "POST" and in_stock:
            quantity = int(request.POST.get('qty', 1))
            if quantity > 0 and quantity <= product.stock:
                # Decrease the stock count
                product.stock -= quantity
                product.save()
                return render(request, "product_detail.html")
            else:
                # Handle the case where the quantity is invalid or exceeds the stock.
                return render(request, "product_detail.html", {
                    'product': product,
                    'latest_product': latest_product,
                    'nested_categories': nested_categories,
                    'in_stock': in_stock,
                    'error_message': "Invalid quantity or insufficient stock.",
                })

        context = {
            'product': product,
            'latest_product': latest_product,
            'nested_categories': nested_categories,
            'in_stock': in_stock,
        }

        return render(request, "product_detail.html", context)

    except Product.DoesNotExist:
        return HttpResponse("Product not found", status=404)
    

#-------------------------------------------------CART--------------------------------------------------


def addToCart(request, pid):
    myli = {"objects":[]}
    try:
        cart = Cart.objects.get(user=request.user)
        myli = json.loads((str(cart.product)).replace("'", '"'))
        try:
            myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) + 1
        except:
            myli['objects'].append({str(pid):1})
        cart.product = myli
        cart.save()
    except:
        myli['objects'].append({str(pid): 1})
        cart = Cart.objects.create(user=request.user, product=myli)
    return redirect('cart')

def incredecre(request, pid):
    cart = Cart.objects.get(user=request.user)
    if request.GET.get('action') == "incre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) + 1
    if request.GET.get('action') == "decre":
        myli = json.loads((str(cart.product)).replace("'", '"'))
        if myli['objects'][0][str(pid)] == 1:
            del myli['objects'][0][str(pid)]
        else:
            myli['objects'][0][str(pid)] = myli['objects'][0].get(str(pid), 0) - 1
    cart.product = myli
    cart.save()
    return redirect('cart')



def cart(request):
    try:
        cart = Cart.objects.get(user=request.user)
        product = (cart.product).replace("'", '"')
        myli = json.loads(str(product))
        product = myli['objects'][0]
        allcategory = Category.objects.all()
        nested_categories = []
        for category in allcategory:
            category_dict = {'category': category, 'subcategories': []}
            subcategories = Subcategory.objects.filter(category=category)
            for subcategory in subcategories:
                    subcategory_dict = {'subcategory': subcategory, 'series': []}

                    # Retrieve series for this subcategory
                    series = Series.objects.filter(brand=subcategory)

                    for s in series:
                        subcategory_dict['series'].append(s)

                    category_dict['subcategories'].append(subcategory_dict)
            nested_categories.append(category_dict)
    
    except:
        product = []
    lengthpro = len(product)
    return render(request, 'cart.html', locals())

def deletecart(request, pid):
    cart = Cart.objects.get(user=request.user)
    product = (cart.product).replace("'", '"')
    myli = json.loads(str(product))
    del myli['objects'][0][str(pid)]
    cart.product = myli
    cart.save()
    messages.success(request, "Delete Successfully")
    return redirect('cart')
#-------------------------------------------------------------wishlist-----------------------------

from .models import WishlistItem
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


@login_required
def wishlist(request, product_id):
    # try:
    product = Product.objects.get(pk=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    messages.info(request, f'Added to Cart')
    return redirect(request.META.get('HTTP_REFERER','home'))

@login_required
def view_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        # Retrieve the categories and nested categories again for the wishlist page
        allcategory = Category.objects.all()
        nested_categories = []
        for category in allcategory:
            category_dict = {'category': category, 'subcategories': []}
            subcategories = Subcategory.objects.filter(category=category)       
            for subcategory in subcategories:
                    subcategory_dict = {'subcategory': subcategory, 'series': []}

                    # Retrieve series for this subcategory
                    series = Series.objects.filter(brand=subcategory)

                    for s in series:
                        subcategory_dict['series'].append(s)

                    category_dict['subcategories'].append(subcategory_dict)
            nested_categories.append(category_dict)        
        for c in nested_categories:
            for s in c.values():
                print(s)
        products = Product.objects.all()
        return render(request, 'wishlist.html', {
            'wishlist_items': wishlist_items,
            'nested_categories': nested_categories,  # Pass the categories to the wishlist template
        })
    else:     
        return redirect('login')

#-------------------------------------------------------------comparison-----------------------------------------

from .models import ComparisonList
@login_required
def add_to_comparison(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user
    comparison_list, created = ComparisonList.objects.get_or_create(user=user)

    if not comparison_list.products.filter(id=product_id).exists():
        comparison_list.products.add(product)
        messages.success(request, "Product added to comparison list.")
    else:
        messages.warning(request, "Product already exists in the comparison list.")

    return redirect('product_detail', pid=product_id)

from django.shortcuts import  get_object_or_404
from .models import ComparisonList

def remove_from_comparison(request, product_id):
    user = request.user
    comparison_list, created = ComparisonList.objects.get_or_create(user=user)
    product = get_object_or_404(Product, pk=product_id)

    if product in comparison_list.products.all():
        comparison_list.products.remove(product)
    
    return redirect('product_comparison')

@login_required
def product_comparison(request):
    try:
        # comparison_list = ComparisonList.objects.get(id=comparison_id)
        user = User.objects.get(id=request.user.id)
        products_to_compare = ComparisonList.objects.all().filter(user=user)
        products = []
        allcategory = Category.objects.all()
        nested_categories = []
        for category in allcategory:
            category_dict = {'category': category, 'subcategories': []}

            subcategories = Subcategory.objects.filter(category=category)

        
            for subcategory in subcategories:
                    subcategory_dict = {'subcategory': subcategory, 'series': []}

                    # Retrieve series for this subcategory
                    series = Series.objects.filter(brand=subcategory)

                    for s in series:
                        subcategory_dict['series'].append(s)

                    category_dict['subcategories'].append(subcategory_dict)
            nested_categories.append(category_dict)
    
# Loop through the comparison_lists and add the products to the products list
        for comparison_list in products_to_compare:
            products.extend(comparison_list.products.all())
        print(products)
        # Debugging: Print the products related to the comparison list
        print('Products in Comparison :', products_to_compare.values())
        return render(request, 'product_comparison.html', {'selectedProducts': products,'nested_categories': nested_categories})
    except ComparisonList.DoesNotExist:
        # Handle the case when the comparison list does not exist
        # Redirect or display an error message as needed
        return HttpResponse('Comparison list not found')



from .models import WishlistItem
from .models import Product  # Import the Product model if not already imported

@login_required
def remove_from_wishlist(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        wishlist_items = WishlistItem.objects.filter(user=request.user, product=product)

        wishlist_items.delete()
        allcategory = Category.objects.all()
        nested_categories = []
        for category in allcategory:
            category_dict = {'category': category, 'subcategories': []}

            subcategories = Subcategory.objects.filter(category=category)

            for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
            nested_categories.append(category_dict)

            products = Product.objects.all()
        # Assuming you have a queryset for wishlist items that you want to pass to the template
        wishlist_items = WishlistItem.objects.filter(user=request.user)

        context = {
            'wishlist_items': wishlist_items,
            'nested_categories': nested_categories,
            'products': products,
            # You can add more context data as needed
        }
        
        return render(request, 'wishlist.html', context)
    
    return redirect('wishlist')  # You can still include the redirect if needed

@login_required
def check_empty_wishlist(request):
    if request.user.is_authenticated:
        wishlist_items = WishlistItem.objects.filter(user=request.user)
        is_empty = not wishlist_items.exists()
        return JsonResponse({"is_empty": is_empty})

def manage_user(request):
    user = UserProfile.objects.all()
    return render(request, 'manage_user.html', locals()) 

def delete_user(request, pid):
    user = User.objects.get(id=pid)
    user.delete()
    messages.success(request, "User deleted successfully")
    return redirect('manage_user') 

def admin_change_password(request):
    if request.method == 'POST':
        o = request.POST.get('currentpassword')
        n = request.POST.get('newpassword')
        c = request.POST.get('confirmpassword')
        user = authenticate(username=request.user.username, password=o)
        if user:
            if n == c:
                user.set_password(n)
                user.save()
                messages.success(request, "Password Changed")
                return redirect('main')
            else:
                messages.success(request, "Password not matching")
                return redirect('admin_change_password')
        else:
            messages.success(request, "Invalid Password")
            return redirect('admin_change_password')
    return render(request, 'admin_change_password.html')


def admin_dashboard(request):
    user = UserProfile.objects.filter()
    category = Category.objects.filter()
    subcategory = Subcategory.objects.filter()
    product = Product.objects.filter()

    return render(request, 'admin_dashboard.html', locals())

from django.http import JsonResponse

#--------------------------------search-----------------------------------------------------

def search_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)
    results = [{'id': product.id, 'name': product.name} for product in products]
    print(results)
    return JsonResponse(results, safe=False)


#--------------------------------------------------------------category validation-------------------------

# mystoreapp/views.py

# from .models import DeliveryAgent


# def add_delivery_agent(request):
#     if request.method == 'POST':
#         form = DeliveryAgentForm(request.POST)
#         if form.is_valid():
#             delivery_agent = form.save(commit=False)
#             delivery_agent.user = request.user  # Assuming you're associating the delivery agent with the currently logged-in user
#             delivery_agent.save()
#             messages.success(request, 'Delivery Agent Added Successfully')
#             return redirect('view_da')
#         else:
#             messages.error(request, 'Error in the form submission. Please check the details.')
#     else:
#         form = DeliveryAgentForm()

#     return render(request, 'add_delivery_agent.html', {'form': form})


# def add_staff_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         # Create a new staff user
#         try:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             messages.success(request, f'Staff {username} added successfully!')
#             return redirect('add_staff')
#         except Exception as e:
#             messages.error(request, f'Error: {e}')

#     return render(request, 'add_staff.html')


from django.db import transaction
from .models import Cart

# from .models import BillingDetails
# @login_required
# @transaction.atomic
# def checkout(request):
#     total_price = 0  # Initialize total_price outside the if block
#     cart_items = Cart.objects.filter(user=request.user)  # Define cart_items here
#     billing_details = None  # Initialize billing_details to None
    
#     # Check if billing details exist for the user
#     if BillingDetails.objects.filter(user=request.user).exists():
#         billing_details = BillingDetails.objects.get(user=request.user)

#     if request.method == 'POST' and 'place_order' in request.POST:
#         # If billing details already exist, you can skip processing the form and just calculate the total price
#         if not billing_details:
#             # Retrieve and process the form data for billing details
#             first_name = request.POST.get('firstname')
#             last_name = request.POST.get('lastname')
#             state = request.POST.get('state')
#             street_address = request.POST.get('streetaddress')
#             apartment_suite_unit = request.POST.get('apartmentsuiteunit')
#             town_city = request.POST.get('towncity')
#             postcode_zip = request.POST.get('postcodezip')
#             phone = request.POST.get('phone')
#             email = request.POST.get('emailaddress')

#             # Create BillingDetails object (assuming BillingDetails is a separate model)
#             billing_details = BillingDetails(
#                 user=request.user,
#                 first_name=first_name,
#                 last_name=last_name,
#                 state=state,
#                 street_address=street_address,
#                 apartment_suite_unit=apartment_suite_unit,
#                 town_city=town_city,
#                 postcode_zip=postcode_zip,
#                 phone=phone,
#                 email=email,
#             )
#             billing_details.save()

#         if cart_items:
#             total_price = sum(item.product.price * item.quantity for item in cart_items)
#         else:
#             total_price = 0
#         for item in cart_items:
#             print(f"Product: {item.product}, Price: {item.product.price}, Quantity: {item.quantity}")


#         # Convert total_price to a float before storing it in the session
#         request.session['order_total'] = float(total_price)

#         # Redirect to the payment page to complete the order
#         return redirect('payment')

#     # If it's not a POST request or not a place order request, continue displaying the cart items
#     total_price = sum(item.product.price * item.quantity for item in cart_items)

#     # Convert total_price to a float before passing it to the template
#     context = {
#         'cart_items': cart_items,
#         'total_price': float(total_price),
#         'billing_details': billing_details,  # Pass billing_details to the template
#     }

#     return render(request, 'cart/checkout.html', context)


#-----------------------------------reg, logi, prof, logout, change paswd -------------------


def registration(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
        mobile = request.POST['mobile']
        image = request.FILES['image']

        # Check if a user with the same email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "A user with this email already exists.")
        else:
            # Create a new user if the email is unique
            user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password, mobile=mobile)
            UserProfile.objects.create(user=user, address=address, image=image)
            messages.success(request, "Registration Successful")
            return redirect('userlogin')
    return render(request, 'registration.html', locals())

# @cache_control(no_cache=True, must_revalidate=True, no_store=True)
# def userlogin(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password=password)
#         if user:
#             if(user.is_staff):
#                 login(request, user)
#                 messages.success(request, "User login successfully")
#                 return redirect('admindashboard')
#             else:
#                 login(request, user)
#                 return redirect('home')
#         else:
#             messages.success(request,"Invalid Credentials")
#     return render(request, 'login.html', locals())



from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_staff and user.is_superuser:
                login(request, user)
                messages.success(request, "Admin login successful")
                return redirect('admindashboard')
            elif user.is_staff:
                login(request, user)
                messages.success(request, "DA login successful")
                return redirect('delivery_agent')
            else:
                login(request, user)
                return redirect('home')
            # else:
            #     login(request, user)
            #     messages.success(request, "DA login successful")
            #     return redirect('delivery_agent')
        else:
            messages.error(request, "Invalid Credentials")

    return render(request, 'login.html')
    
@login_required
def delivery_agent(request):   
    return render(request, 'view_assigned_orders.html', locals())


@login_required
def profile(request):
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}
        subcategories = Subcategory.objects.filter(category=category)
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)
                for s in series:
                    subcategory_dict['series'].append(s)
                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
        
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # If UserProfile doesn't exist, create a new one for the user
        user_profile = UserProfile(user=user)
        user_profile.save()

    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')       
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if fname:
            user.first_name = fname
        if lname:
            user.last_name = lname
        if mobile:
            user_profile.mobile = mobile
        if address:
            user_profile.address = address
        if image:
            user_profile.image = image

        # Save changes to user and user profile
        user.save()
        user_profile.save()

        messages.success(request, "Profile updated")
        return redirect('profile')

    return render(request, 'profile.html', {'user_profile': user_profile, 'user': user})


    # return render(request, 'profile.html')

def logoutuser(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('home')

def change_password(request):
    if request.method == 'POST':
        o = request.POST.get('old')
        n = request.POST.get('new')
        c = request.POST.get('confirm')
        user = authenticate(username=request.user.username, password=o)
        if user:
            if n == c:
                user.set_password(n)
                user.save()
                messages.success(request, "Password Changed")
                return redirect('main')
            else:
                messages.success(request, "Password not matching")
                return redirect('change_password')
        else:
            messages.success(request, "Invalid Password")
            return redirect('change_password')
    return render(request, 'change_password.html')






#-----------------------Booking Details------------------------------------------------------------------


import json
from .models import Booking, Product, Cart

# def booking(request):
#     user = request.user
#     cart = Cart.objects.get(user=user)
#     total = 0
#     productid = cart.product.replace("'", '"')
#     productid = json.loads(str(productid))
    
#     try:
#         productid = productid['objects'][0]
#     except:
#         messages.success(request, "Cart is empty, Please add a product to the cart.")
#         return redirect('cart')
    
#     for i, quantity in productid.items():
#         product = Product.objects.get(id=i)
#         total += int(quantity) * int(product.price)
    
#     if request.method == "POST":
#         # Assuming that the fields are in the Booking model
#         state = request.POST.get('state')  # Replace with the actual names used in the form
#         street_address = request.POST.get('street_address')
#         apartment_suite_unit = request.POST.get('apartment_suite_unit')
#         town_city = request.POST.get('town_city')
#         postcode_zip = request.POST.get('postcode_zip')
        
#         # Create a Booking object
#         book = Booking.objects.create(
#             user=user,
#             product=cart.product,
#             total=total,
#             state=state,
#             street_address=street_address,
#             apartment_suite_unit=apartment_suite_unit,
#             town_city=town_city,
#             postcode_zip=postcode_zip,
#         )

#         # Reset the cart product to an empty list
#         cart.product = {'objects': []}
#         cart.save()

#         messages.success(request, "Order booked successfully")
#         return redirect('main')
    
#     return render(request, "booking.html", locals())

from mystoreapp.models import UserProfile  # Replace 'your_app_name' with the actual name of your app

@login_required
def booking(request):
    user = request.user
    cart = Cart.objects.get(user=user)
    total = 0
    productid = cart.product.replace("'", '"')
    productid = json.loads(str(productid))
    try:
        productid = productid['objects'][0]
    except:
        messages.success(request, "Cart is empty, Please add a product to the cart.")
        return redirect('cart') 
    for i,j in productid.items():
        product = Product.objects.get(id=i)
        total += int(j) * int(product.price)
    # Fetch user profile data
    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        # Handle the case where the profile does not exist
        user_profile = None

    if request.method == "POST":
        # Assuming that the fields are in the Booking model
        state = request.POST.get('state')  # Replace with the actual names used in the form
        street_address = request.POST.get('street_address')
        apartment_suite_unit = request.POST.get('apartment_suite_unit')
        town_city = request.POST.get('town_city')
        postcode_zip = request.POST.get('postcode_zip')
        
        # Create a Booking object
        book = Booking.objects.create(
            user=user,
            product=cart.product,
            total=total,
            state=state,
            street_address=street_address,
            apartment_suite_unit=apartment_suite_unit,
            town_city=town_city,
            postcode_zip=postcode_zip,
        )

        # Reset the cart product to an empty list
        cart.product = {'objects': []}
        cart.save()

        messages.success(request, "Order booked successfully")
        return redirect('/payment/?total='+str(total))
    
    return render(request, "booking.html", {'user': user, 'cart': cart, 'total': total, 'user_profile': user_profile})



def myOrder(request):
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}

        subcategories = Subcategory.objects.filter(category=category)

       
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
    order = Booking.objects.filter(user=request.user)
    return render(request, "my-order.html", locals())


def user_order_track(request, pid):
    allcategory = Category.objects.all()
    nested_categories = []
    for category in allcategory:
        category_dict = {'category': category, 'subcategories': []}

        subcategories = Subcategory.objects.filter(category=category)

       
        for subcategory in subcategories:
                subcategory_dict = {'subcategory': subcategory, 'series': []}

                # Retrieve series for this subcategory
                series = Series.objects.filter(brand=subcategory)

                for s in series:
                    subcategory_dict['series'].append(s)

                category_dict['subcategories'].append(subcategory_dict)
        nested_categories.append(category_dict)
    order = Booking.objects.get(id=pid)
    orderstatus = ORDERSTATUS
    return render(request, "user-order-track.html", locals())

def change_order_status(request, pid):
    order = Booking.objects.get(id=pid)
    status = request.GET.get('status')
    if status:
        order.status = status
        order.save()
        messages.success(request, "Order status changed.")
    return redirect('myorder')

def payment(request):
    total = request.GET.get('total')
    cart = Cart.objects.get(user=request.user)
    if request.method == "POST":
        book = Booking.objects.create(user=request.user, product=cart.product, total=total)
        cart.product = {'objects': []}
        cart.save()
        messages.success(request, "Ordered Successfully")
        return redirect('myorder')
    return render(request, 'payment.html', locals())

def manage_order(request):
    action = request.GET.get('action', 0)
    order = Booking.objects.filter(status=int(action))
    order_status = ORDERSTATUS[int(action)-1][1]
    if int(action) == 0:
        order = Booking.objects.filter()
        order_status = 'All'
    return render(request, 'manage_order.html', locals()) 

def delete_order(request, pid):
    order = Booking.objects.get(id=pid)
    order.delete()
    messages.success(request, 'Order Deleted')
    return redirect('/manage-order/?action='+request.GET.get('action'))




#-------------------------------------------Delivery Agent--------------------------------------------
# def regdelivery(request):
#     if request.method == 'POST':
#         # Retrieve data from the form
#         name = request.POST.get('name')
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         license_number = request.POST.get('license')
#         vechicle_type = request.POST.get('vechicle_type')
#         location = request.POST.get('location')
#         password = request.POST.get('password')

#         # Use the custom manager to create a new user
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password,
#         )

#         # Create a new DeliveryAgent instance with 'pending' status
#         delivery_agent = DeliveryAgent.objects.create(
#             user=user,  # Associate the DeliveryAgent with the user
#             name=name,
#             username=username,
#             email=email,
#             phone=phone,
#             license_number=license_number,
#             vechicle_type=vechicle_type,
#             location=location,
#             status='pending',  # Set the status to 'pending'
#         )

#         # Redirect to a success page or do other actions as needed
#         return redirect('login')

#     return render(request, 'regdelivery.html')





#------------------------------------------------------------ADMIN--------------------------------------
#admin related 

def adminLogin(request):
    msg = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        try:
            if user.is_staff:
                login(request, user)
                msg = "User login successfully"
                return redirect('admindashboard')
            else:
                msg = "Invalid Credentials"
        except:
            msg = "Invalid Credentials"
    dic = {'msg': msg}
    return render(request, 'admin_login.html', dic)

def adminHome(request):
    return render(request, 'admin_base.html')

def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
#-------------------------------------------------------DELIVERY AGENT--------------------------


from django.core.mail import send_mail
from .models import DeliveryAgent


# @login_required
# def add_da(request):
#     print(12323)
#     if request.method == 'POST':
#         # Extract form data
#         agent_name = request.POST.get('agent_name')
#         place = request.POST.get('place')
#         mobile_number = request.POST.get('mobile')
#         pincode = request.POST.get('pincode')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Create user
#         print(email)
#         user = User.objects.create_user(username=email, email=email, password=password)
#         print(123,user)
#         user.first_name = agent_name
#         user.save()

#         # Create delivery agent
#         delivery_agent = DeliveryAgent.objects.create(
#             user=user,
#             place=place,
#             pincode=pincode,
#             location=place,
#         )

#         # Send email notification
#         subject = 'Welcome to TechTrove Delivery Team'
#         message = f'Hi {agent_name},\n\nYou have been added as a delivery agent on TechTrove.\n\nYour login credentials:\nEmail: {email}\nPassword: {password}\n\nThank you for joining our team!'
#         from_email = 'mailtoshowvalidationok@gmail.com'  # Replace with your email
#         recipient_list = [email]

#         send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
#         # Display success message and redirect
#         messages.success(request, 'Agent Added Successfully')
#         return redirect('view_da')

#     return render(request, 'add_staff.html')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import DeliveryAgent  # Import your DeliveryAgent model

@login_required
def add_da(request):
    if request.method == 'POST':
        # Extract form data
        agent_name = request.POST.get('agent_name')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')  # Using consistent variable name
        pincode = request.POST.get('pincode')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            # Check if user with provided email already exists
            existing_user = User.objects.get(email=email)
            # User already exists, handle this case (e.g., display error message)
            messages.error(request, 'User with this email already exists')
            return redirect('view_da')  # Assuming 'view_da' is the URL name for viewing delivery agents
        except User.DoesNotExist:
            # User does not exist, proceed with creating new user
            pass
        
        # Create user
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = agent_name
        user.is_staff = True
        user.save()

        # Create delivery agent
        delivery_agent = DeliveryAgent.objects.create(
            user=user,
            place=place,
            mobile=mobile,  # Using consistent variable name
            pincode=pincode,
            location=place,  # Is this correct? You're assigning place to both place and location
        )

        # Send email notification
        subject = 'Welcome to TechTrove Delivery Team'
        message = f'Hi {agent_name},\n\nYou have been added as a delivery agent on TechTrove.\n\nYour login credentials:\nEmail: {email}\nPassword: {password}\n\nThank you for joining our team!'
        from_email = 'mailforgranted@gmail.com'  # Replace with your email
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        
        # Display success message and redirect
        messages.success(request, 'Agent Added Successfully')
        return redirect('view_da')  # Assuming 'view_da' is the URL name for viewing delivery agents

    return render(request, 'add_staff.html')  # Assuming 'add_staff.html' is the template for adding a delivery agent


# def add_da(request):
#     if request.method == 'POST':
#         # Extract form data
#         agent_name = request.POST.get('agent_name')
#         place = request.POST.get('place')
#         mobile_number = request.POST.get('mobile')
#         pincode = request.POST.get('pincode')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Check if email is not empty
#         if not email:
#             messages.error(request, 'Email is required')
#             return redirect('add_da')

#         # Create user with email as username
#         try:
#             user = User.objects.create_user(username=email, email=email, password=password)
#             user.first_name = agent_name
#             user.save()

#             # Create delivery agent
#             delivery_agent = DeliveryAgent.objects.create(
#                 user=user,
#                 place=place,
#                 pincode=pincode,
#                 location=place,
#             )

#             # Send email notification
#             subject = 'Welcome to TechTrove Delivery Team'
#             message = f'Hi {agent_name},\n\nYou have been added as a delivery agent on TechTrove.\n\nYour login credentials:\nEmail: {email}\nPassword: {password}\n\nThank you for joining our team!'
#             from_email = 'mailtoshowvalidationok@gmail.com'  # Replace with your email
#             recipient_list = [email]

#             send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
#             # Display success message and redirect
#             messages.success(request, 'Agent Added Successfully')
#             return redirect('view_da')
#         except Exception as e:
#             messages.error(request, f'Error occurred: {e}')
#             return redirect('add_da')

#     return render(request, 'add_staff.html')


def view_da(request):
    
    delivery_agents = DeliveryAgent.objects.all()
    
    context = {
        'delivery_agents': delivery_agents,
    }
    return render(request, 'delivery_agent_list.html', context)

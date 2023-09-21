import json
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import cache_control
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request, 'navigation.html')

def about(request):
    return render(request, 'about.html')

from .models import Carousel, Cart, Subcategory, UserProfile
def main(request):
    data = Carousel.objects.all()
    dic = {'data':data}
    return render(request, 'index.html', dic)

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

# <------------------------------------------------Category------------------------

from .models import Category
def add_category(request):
    if request.method == "POST":
        name = request.POST['name']
        Category.objects.create(name=name)
        msg = "Category added"
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

def add_subcategory(request):
    category = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        cat = request.POST['category']
        Subcategory.objects.create(name=name)
        messages.success(request, "SubCategory added")
        catobj = Category.objects.get(id=cat)
        return redirect('view_subcategory')
    return render(request, 'add_subcategory.html', locals())


def edit_subcategory(request, pid):
    subcategory = Subcategory.objects.get(id=pid)
    if request.method == "POST":
        name = request.POST['name']
        subcategory.name = name
        subcategory.save()
        msg = "SubCategory Updated"
    return render(request, 'edit_subcategory.html', locals())

def delete_subcategory(request, pid):
    subcategory = Subcategory.objects.get(id=pid)
    subcategory.delete()
    return redirect('view_subcategory')

def view_subcategory(request):
    subcategory = Subcategory.objects.all()
    return render(request, 'view_subcategory.html', locals())

# ------------------------------------------Product-------------------

from .models import Product
def add_product(request):
    category = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        cat = request.POST['category']
        discount = request.POST['discount']
        desc = request.POST['desc']
        image = request.FILES['image']
        catobj = Category.objects.get(id=cat)
        Product.objects.create(name=name, price=price, discount=discount, category=catobj, description=desc, image=image)
        messages.success(request, "Product added")
    return render(request, 'add_product.html', locals())


def view_product(request):
    product = Product.objects.all()
    return render(request, 'view_product.html', locals())


def edit_product(request, pid):
    product = Product.objects.get(id=pid)
    category = Category.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        price = request.POST['price']
        cat = request.POST['category']
        discount = request.POST['discount']
        desc = request.POST['desc']
        try:
            image = request.FILES['image']
            product.image = image
            product.save()
        except:
            pass
        catobj = Category.objects.get(id=cat)
        Product.objects.filter(id=pid).update(name=name, price=price, discount=discount, category=catobj, description=desc)
        messages.success(request, "Product Updated")
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






# -----------------------------------------registration,userlogin,profile,logout----------
# def registration(request):
    
#     if request.method == "POST":
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#         password = request.POST['password']
#         address = request.POST['address']
#         mobile = request.POST['mobile']
#         image = request.FILES['image']
#         user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password)
#         UserProfile.objects.create(user=user, mobile=mobile, address=address, image=image)
#         messages.success(request, "Registeration Successful")
#     return render(request, 'registration.html', locals())


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
            user = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=password)
            UserProfile.objects.create(user=user, mobile=mobile, address=address, image=image)
            messages.success(request, "Registration Successful")
            return redirect('userlogin')
    return render(request, 'registration.html', locals())

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if(user.is_staff):
                login(request, user)
                messages.success(request, "User login successfully")
                return redirect('admindashboard')
            else:
                login(request, user)
                return redirect('home')
        else:
            messages.success(request,"Invalid Credentials")
    return render(request, 'login.html', locals())


def profile(request):
    data = UserProfile.objects.get(user=request.user)
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        address = request.POST['address']
        mobile = request.POST['mobile']
        try:
            image = request.FILES['image']
            data.image = image
            data.save()
        except:
            pass
        user = User.objects.filter(id=request.user.id).update(first_name=fname, last_name=lname)
        UserProfile.objects.filter(id=data.id).update(mobile=mobile, address=address)
        messages.success(request, "Profile updated")
        return redirect('profile')
    return render(request, 'profile.html', locals())



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




def user_product(request,pid):
    if pid == 0:
        product = Product.objects.all()
    else:
        category = Category.objects.get(id=pid)
        product = Product.objects.filter(category=category)
    allcategory = Category.objects.all()
    return render(request, "user-product.html", locals())



def product_detail(request, pid):
    product = Product.objects.get(id=pid)
    latest_product = Product.objects.filter().exclude(id=pid).order_by('-id')[:10]
    return render(request, "product_detail.html", locals())



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
 

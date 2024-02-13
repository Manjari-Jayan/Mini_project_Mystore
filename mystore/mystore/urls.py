
from django import views
from django.contrib import admin
from django.urls import include, path
from mystoreapp.views import *


# from mystoreapp.views import  check_empty_wishlist, delete_series, edit_series, home,index,about,main, remove_from_wishlist, series_product, three, view_series, view_wishlist, wishlist
# from mystoreapp.views import adminHome,admin_dashboard,adminLogin,add_category,view_category, search_products
# from mystoreapp.views import edit_category,delete_category,add_product,view_product, delete_product,edit_product,add_subcategory,view_subcategory,edit_subcategory,delete_subcategory,add_series
# from mystoreapp.views import registration,userlogin,profile,change_password,user_product,brand_product,product_detail, addToCart, cart,incredecre,deletecart,manage_user,delete_user,admin_change_password,logoutuser
from django.conf import settings
from django.conf.urls.static import static
# from .views import add_delivery_agent

urlpatterns = [
    path('admin/', admin.site.urls),
 
    path('', home, name="home"),
    path('index/', index, name="index"),
    path('three/', three, name="three"),
    path('about/', about, name="about"),
    # path('main/', main, name="main"),
    path('adminhome/', adminHome, name="adminhome"),
    path('admindashboard/', admin_dashboard, name="admindashboard"),
    path('admin-login/', adminLogin, name="admin_login"),
    path('add-category/', add_category, name="add_category"),
    path('view-category/', view_category, name="view_category"),
    path('edit-category/<int:pid>/', edit_category, name="edit_category"),
    path('delete-category/<int:pid>/', delete_category, name="delete_category"),
    path('add-product/', add_product, name='add_product'),
    path('view-product/', view_product, name='view_product'),
    path('edit-product/<int:pid>/', edit_product, name="edit_product"),
    path('delete-product/<int:pid>/', delete_product, name="delete_product"),

    path('add-subcategory/', add_subcategory, name="add_subcategory"),
    path('view-subcategory/', view_subcategory, name="view_subcategory"),
    path('edit-subcategory/<int:pid>/', edit_subcategory, name="edit_subcategory"),
    path('delete-subcategory/<int:pid>/', delete_subcategory, name="delete_subcategory"),
    path('add-series/', add_series, name="add_series"),
    path('view-series/', view_series, name="view_series"),
    path('edit-series/<int:pid>/', edit_series, name="edit_series"),
    path('delete-series/<int:pid>/', delete_series, name="delete_series"),
    path('search-products/', search_products, name='search_products'),
    
    # path('search-autofill/', search_autofill, name='search_autofill'),
    # path('search/', search_products, name='search_products'),
    # path('search-suggestions/', search_suggestions, name='search_suggestions'),
    path('registration/', registration, name="registration"),
    path('userlogin/', userlogin, name="userlogin"),
    path('profile/', profile, name="profile"),
    path('change-password/', change_password, name="change_password"),
    path('user-product/<int:pid>/', user_product, name="user_product"),
    path('brand/<int:pid>/', brand_product, name="brand_product"),
    path('series/<int:pid>/', series_product, name="series_product"),
    path('product-detail/<int:pid>/', product_detail, name="product_detail"),
    path('wishlist/<int:product_id>/', wishlist, name='wishlist'),
    path('remove_from_wishlist/<int:product_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('check_empty_wishlist/', check_empty_wishlist, name='check_empty_wishlist'),
    path('view_wishlist/', view_wishlist, name='view_wishlist'),
#    path('view_wishlist/<int:product_id>/', view_wishlist, name='view_wishlist'),

    # path('wishlist/', wishlist, name="wishlist"),
    path('manage-user/', manage_user, name="manage_user"),
    path('delete-user/<int:pid>/', delete_user, name="delete_user"),
    path('admin-change-password/',admin_change_password, name="admin_change_password"),
    path('logout/', logoutuser, name="logout"),
    path('add_to_comparison/<int:product_id>/', add_to_comparison, name='add_to_comparison'),
    path('remove_from_comparison/<int:product_id>/', remove_from_comparison, name='remove_from_comparison'),
    path('product_comparison', product_comparison, name='product_comparison'),
   
    path('add-to-cart/<int:pid>/', addToCart, name="addToCart"),
    path('cart/', cart, name="cart"),
    path('incredecre/<int:pid>/', incredecre, name="incredecre"),
    path('deletecart/<int:pid>/', deletecart, name="deletecart"),
    # path('add_staff/', add_da, name='add_staff'),
    path('booking/', booking, name="booking"),
    path('my-order/', myOrder, name="myorder"),
    path('user_order_track/<int:pid>/', user_order_track, name="user_order_track"),
    path('change-order-status/<int:pid>/', change_order_status, name="change_order_status"),
    path('payment/', payment, name="payment"),
    path('manage-order/', manage_order, name="manage_order"),
    path('delete-order/<int:pid>/', delete_order, name="delete_order"),
    path('delivery_agent/', delivery_agent, name='delivery_agent'),
    

    # path('add_da/', add_da, name='add_da'),
    # path('view_da/', view_da, name='view_da'),
    path('admin-order-track/<int:pid>/', admin_order_track, name="admin_order_track"),
    path('user-feedback/', user_feedback, name="user_feedback"),
    path('manage-feedback/', manage_feedback, name="manage_feedback"),
    path('delete-feedback/<int:pid>/', delete_feedback, name="delete_feedback"),
    path('feedback-read/<int:pid>/', read_feedback, name="read_feedback"),
    path('regdelivery', regdelivery, name="regdelivery"),
    path('deliveryagent', deliveryagent, name="deliveryagent"),
    path('approve_delivery_agent/<int:agent_id>/', approve_delivery_agent, name='approve_delivery_agent'),
    path('reject_delivery_agent/<int:agent_id>/', reject_delivery_agent, name='reject_delivery_agent'),
    path('deliverylogin', deliverylogin, name="deliverylogin"),
    path('deliverydetails', deliverydetails, name="deliverydetails"),
    # path('checkout/', checkout, name='checkout'),
    # path('add_delivery_agent/', add_delivery_agent, name='add_delivery_agent'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

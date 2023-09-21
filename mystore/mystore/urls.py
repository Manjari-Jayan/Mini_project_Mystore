
from django.contrib import admin
from django.urls import path
from mystoreapp.views import home,index,about,main
from mystoreapp.views import adminHome,admin_dashboard,adminLogin,add_category,view_category
from mystoreapp.views import edit_category,delete_category,add_product,view_product, delete_product,edit_product,add_subcategory,view_subcategory,edit_subcategory,delete_subcategory
from mystoreapp.views import registration,userlogin,profile,change_password,user_product,product_detail, addToCart, cart,incredecre,deletecart,manage_user,delete_user,admin_change_password,logoutuser
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('index/', index, name="index"),
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
    # path('add-subproduct/', add_subproduct, name='add_subproduct'),
    # path('view-subproduct/', view_subproduct, name='view_subproduct'),
    # path('edit-subproduct/<int:pid>/', edit_subproduct, name="edit_subproduct"),
    # path('delete-subproduct/<int:pid>/', delete_subproduct, name="delete_subproduct"),
    
    path('registration/', registration, name="registration"),
    path('userlogin/', userlogin, name="userlogin"),
    path('profile/', profile, name="profile"),
    path('change-password/', change_password, name="change_password"),
    path('user-product/<int:pid>/', user_product, name="user_product"),
    path('product-detail/<int:pid>/', product_detail, name="product_detail"),
    path('add-to-cart/<int:pid>/', addToCart, name="addToCart"),
    path('cart/', cart, name="cart"),
    path('incredecre/<int:pid>/', incredecre, name="incredecre"),
    path('deletecart/<int:pid>/', deletecart, name="deletecart"),
    path('manage-user/', manage_user, name="manage_user"),
    path('delete-user/<int:pid>/', delete_user, name="delete_user"),
    path('admin-change-password/',admin_change_password, name="admin_change_password"),
    path('logout/', logoutuser, name="logout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
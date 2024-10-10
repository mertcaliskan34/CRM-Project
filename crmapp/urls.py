from django.urls import path

from . import views

urlpatterns = [
     
     path('', views.home, name=""),
     
     path('register', views.register, name="register"),
     
     path('my-login', views.my_login, name="my-login"),
     
     path('user-logout', views.user_logout, name="user-logout"),
     
     path('about', views.about, name="about"),
     
     path('terms-service', views.terms_service, name="terms-service"),
     
     # CRUD
     
     path('dashboard', views.dashboard, name="dashboard"),
     
     path('create-record', views.create_record, name="create-record"),
     
     path('update-record/<int:pk>', views.update_record, name="update-record"),
     
     path('record/<int:pk>', views.singular_record, name="record"),
     
     path('delete-record/<int:pk>', views.delete_record, name="delete-record"),
     
     path('products', views.products, name="products"),
     
     path('add-product', views.add_product, name="add-product"),
     
     path('update-product/<int:pk>', views.update_product, name="update-product"),
     
     path('view-product/<int:pk>', views.singular_product, name="product"),
     
     path('delete-product/<int:pk>', views.delete_product, name="delete-product"),
     
     path('create-order', views.create_order, name="create-order"),
     
     path('update-order/<int:pk>', views.update_order, name="update-order"),
     
     path('view-order/<int:pk>', views.singular_order, name="order"),
     
     path('delete-order/<int:pk>', views.delete_order, name="delete-order"),
]
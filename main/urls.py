from django.urls import path
from . import views
from .views import (
    MenuListView,
    menu,
    menuDetail,
    add_to_cart,
    get_cart_items,
    order_item,
    CartDeleteView,
    order_details,
)

app_name = "main"

urlpatterns = [
    path('', MenuListView.as_view(), name='home'),
    path('menu/', menu, name='menu'),
    path('dishes/<slug>', menuDetail, name='dishes'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('cart/', get_cart_items, name='cart'),
    path('remove-from-cart/<int:pk>/', CartDeleteView.as_view(), name='remove-from-cart'),
    path('ordered/', order_item, name='ordered'),
    path('order_details/', order_details, name='order_details'),
    path('about/', views.about, name='about'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
]
